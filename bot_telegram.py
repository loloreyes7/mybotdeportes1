import os
import requests
from telegram import Bot
import asyncio
from urllib.parse import urlparse

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Usamos una lista para construir la URL, esto elimina cualquier \n oculto
url_parts = [
    "https://jack33eo.mp7786j2ncsusov57",
    "general.ru/es/football/conmebol-copa-libertadores-4375787/",
    "rosario-central-vs-universidad-central-de-venezuela.html?icg=RVM&ilang=es"
]
URL = "".join(url_parts)

async def main():
    bot = Bot(token=TOKEN)
    try:
        # Validación: esto fallará antes de intentar conectar si la URL es inválida
        result = urlparse(URL)
        if not all([result.scheme, result.netloc]):
            print("La URL generada es inválida.")
            return

        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            await bot.send_message(chat_id=CHAT_ID, text="✅ ¡Conexión exitosa!")
        else:
            print(f"Error HTTP: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
