# SITE_ITALIANO

Aplicativo Django para estudar italiano com repetição espaçada usando frases curtas de
Alice no País das Maravilhas.

Para continuar o projeto em outro chat, leia primeiro:

```text
PROJECT_CONTEXT.md
```

## Rodar localmente

```powershell
python manage.py migrate
python manage.py seed_chapter_one
python manage.py runserver 127.0.0.1:8000
```

Depois abra:

```text
http://127.0.0.1:8000/
```

## Deploy no VPS

Instalar ou atualizar o atalho no VPS:

```bash
cd /var/www/site_idiomas
sudo install -m 755 scripts/update_vps.sh /usr/local/bin/atualizar-site-idiomas
```

Depois, para publicar uma nova versao:

```bash
atualizar-site-idiomas
```
