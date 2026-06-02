# Contexto do Projeto SITE_ITALIANO

Este documento guarda o contexto para continuar o projeto em outro chat.
Sempre que houver uma alteracao relevante no projeto, atualizar este arquivo,
fazer commit no Git e enviar para o GitHub.

## Objetivo

Criar um aplicativo Django/Python parecido com Anki, focado em aprender italiano
com base no livro "Le avventure di Alice nel paese delle meraviglie".

O estudo acontece em ordem linear do livro:

1. O livro e dividido em cards curtos, com frases de no maximo 5 palavras.
2. O usuario estuda os cards em ordem.
3. Cada card usa repeticao espacada.
4. A tela "Ler" mostra, na ordem do livro, todas as frases que ja apareceram
   para aquele usuario estudar.
5. Conforme novos blocos forem estudados, os proximos cards do capitulo serao
   cadastrados.

## Fonte

O PDF do livro esta na pasta do projeto local:

`le-avventure-di-alice-nel-paese-delle-meraviglie-alice-no-pais-das-maravilhas-lewis-carroll.pdf`

O PDF esta versionado no GitHub porque o usuario pediu para subir o arquivo
para a nuvem junto com o projeto.

## Stack

- Python 3.14
- Django 6
- SQLite local
- App Django principal: `study`
- Projeto Django: `aliceanki`

## Como Rodar

```powershell
cd "C:\Users\fabiano.polone\Documents\AKI FABIANO"
python manage.py migrate
python manage.py seed_chapter_one
python manage.py runserver 127.0.0.1:8000
```

Abrir:

```text
http://127.0.0.1:8000/
```

## Funcionalidades Ja Criadas

- Login obrigatorio ao abrir o site.
- Cadastro com usuario, senha e repetir senha.
- Cada usuario tem progresso proprio.
- 40 cards iniciais do Capitulo I.
- Botao Play na frase principal usando `SpeechSynthesis` do navegador em italiano.
- Botao Play nos exemplos de presente, passado e futuro.
- Repeticao espacada simples inspirada no Anki:
  - `Errei`: volta mais tarde, em cerca de 10 minutos.
  - `Dificil`: marca aprendido e agenda revisao curta.
  - `Bom`: marca aprendido e agenda revisao normal.
  - `Facil`: marca aprendido e agenda revisao mais distante.
- A tela "Ler" mostra frases que ja apareceram para estudo, nao apenas frases
  acertadas.
- Frases relacionadas no card atual:
  - mostra outras frases do lote com mesmo verbo;
  - mostra outras frases com formas do verbo em outro tempo;
  - mostra palavras parecidas/compartilhadas relevantes;
  - cada frase relacionada tambem tem Play.

## Arquivos Importantes

- `study/models.py`: modelos `Segment` e `ReviewState`.
- `study/views.py`: login, cadastro, estudo, leitura e frases relacionadas.
- `study/templates/study/study_card.html`: tela principal do card.
- `study/templates/study/read_learned.html`: leitura desbloqueada.
- `study/static/study/app.js`: audio com `SpeechSynthesis`.
- `study/static/study/styles.css`: visual do app.
- `study/management/commands/seed_chapter_one.py`: carrega os 40 cards iniciais.

## Regras De Continuidade

- Sempre manter os cards em ordem do livro.
- Cada card deve ter frase curta, idealmente ate 5 palavras.
- Quando houver verbo, preencher:
  - verbo principal;
  - exemplo no presente;
  - exemplo no passado;
  - exemplo no futuro.
- O botao "Ler" deve usar frases ja vistas/abertas pelo usuario, em ordem.
- Nao versionar `db.sqlite3`, caches ou ambientes virtuais.
- O PDF do livro deve permanecer versionado no repositorio.
- A cada alteracao relevante:
  1. Atualizar este documento se a decisao mudar ou algo novo for criado.
  2. Rodar `python manage.py check`.
  3. Fazer commit com mensagem clara.
  4. Fazer push para `origin main`.

## GitHub

Remote:

```text
https://github.com/fabianopolone123/SITE_ITALIANO.git
```

Branch principal:

```text
main
```

## Historico Resumido

- Primeiro commit: app Django inicial com repeticao espacada, login/cadastro,
  40 cards do Capitulo I, audio e leitura desbloqueada.
- Depois foi ajustada a leitura para aparecer quando o card e aberto, nao apenas
  quando e acertado.
- Depois foram adicionadas frases relacionadas no card.
- Depois a relacao foi melhorada para considerar formas do verbo em outros
  tempos, como presente, passado e futuro.
- Depois o PDF do livro foi incluido no GitHub junto com o projeto.
- Depois o projeto foi preparado para deploy no VPS usando variaveis de ambiente
  `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS` e
  `DJANGO_CSRF_TRUSTED_ORIGINS`, com `STATIC_ROOT` para `collectstatic`.
- Depois foi criado `scripts/update_vps.sh`, instalado no VPS como
  `/usr/local/bin/atualizar-site-idiomas`, para atualizar o projeto novo,
  executar migrations, `seed_chapter_one`, `collectstatic`, `check` e reiniciar
  o servico `site_idiomas`.
