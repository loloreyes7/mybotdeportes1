import os
import requests
from telegram import Bot
import asyncio

# Obtiene los secretos
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
# Definimos la URL de forma limpia
URL = "https://jack33eo.mp7786j2ncsusov57general.ru/es/football/conmebol-copa-libertadores-4375787/rosario-central-vs-universidad-central-de-venezuela.html?icg=RVM&ilang=es"

async def main():
    if not TOKEN or not CHAT_ID:
        print("Error: Credenciales no cargadas.")
        return

    bot = Bot(token=TOKEN)
    try:
        # Usamos una cabecera para que la web no rechace al bot
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            await bot.send_message(chat_id=CHAT_ID, text=f"✅ Bot conectado correctamente.\nEstado de la web: {response.status_code}")
            print("Mensaje enviado correctamente.")
        else:
            print(f"La web respondió con código: {response.status_code}")
            
    except Exception as e:
        print(f"Error técnico: {e}")

if __name__ == "__main__":
    asyncio.run(main())
