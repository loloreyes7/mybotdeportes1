import os
import requests
from telegram import Bot
import asyncio

# Obtiene los secretos
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Construimos la URL por partes para evitar el error de salto de línea
parte1 = "https://jack33eo.mp7786j2ncsusov57general.ru/es/football/"
parte2 = "conmebol-copa-libertadores-4375787/rosario-central-vs-universidad-central-de-venezuela.html"
parte3 = "?icg=RVM&ilang=es"
URL = parte1 + parte2 + parte3

async def main():
    if not TOKEN or not CHAT_ID:
        print("Error: Credenciales no cargadas.")
        return

    bot = Bot(token=TOKEN)
    try:
        # User-Agent para parecer un navegador real
        headers = {'User-Agent': 'Mozilla/5.0'}
        print(f"Intentando conectar a: {URL}")
        
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            await bot.send_message(chat_id=CHAT_ID, text="✅ ¡Conexión exitosa con la web!")
            print("Mensaje enviado correctamente.")
        else:
            print(f"La web respondió con código: {response.status_code}")
            
    except Exception as e:
        print(f"Error técnico: {e}")

if __name__ == "__main__":
    asyncio.run(main())
