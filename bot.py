name: Ejecutar Bot de Deportes
on:
schedule:
- cron: '*/30 * * * *' # Se ejecuta cada 30 minutos
workflow_dispatch: # Permite ejecutarlo manualmente desde GitHub

jobs:
build:
runs-on: ubuntu-latest
steps:
- name: Checkout repo
uses: actions/checkout@v3

  - name: Setup Python
    uses: actions/setup-python@v4
    with:
      python-version: '3.9'

  - name: Instalar dependencias
    run: pip install -r requirements.txt

  - name: Ejecutar Bot
    env:
      TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
      CHAT_ID: ${{ secrets.CHAT_ID }}
    run: python bot_deportes.py



        