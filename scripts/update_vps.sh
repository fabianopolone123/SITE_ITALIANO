#!/usr/bin/env bash
set -euo pipefail

PROJECT_DIR="${PROJECT_DIR:-/var/www/site_idiomas}"
SERVICE_NAME="${SERVICE_NAME:-site_idiomas}"
BRANCH="${BRANCH:-main}"
REMOTE_URL="${REMOTE_URL:-https://github.com/fabianopolone123/SITE_ITALIANO.git}"

cd "$PROJECT_DIR"

echo "==> Atualizando codigo"
git remote set-url origin "$REMOTE_URL"
git fetch origin "$BRANCH"
git reset --hard "origin/$BRANCH"

echo "==> Ativando ambiente virtual"
source .venv/bin/activate

echo "==> Instalando dependencias"
pip install -r requirements.txt

echo "==> Garantindo WSGI do projeto novo no servico"
if systemctl cat "$SERVICE_NAME" | grep -q 'config\.wsgi:application'; then
    sed -i 's/config\.wsgi:application/aliceanki.wsgi:application/g' "/etc/systemd/system/${SERVICE_NAME}.service"
    systemctl daemon-reload
fi

echo "==> Aplicando migrations"
python manage.py migrate --noinput

echo "==> Carregando cards do capitulo"
python manage.py seed_chapter_one

echo "==> Coletando arquivos static"
python manage.py collectstatic --noinput

echo "==> Checando Django"
python manage.py check

echo "==> Reiniciando servico"
systemctl restart "$SERVICE_NAME"
systemctl --no-pager --lines=12 status "$SERVICE_NAME"

echo "==> Deploy concluido"
