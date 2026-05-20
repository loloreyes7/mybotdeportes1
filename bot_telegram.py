import os
import requests
from telegram import Bot
import asyncio

# Obtiene los secretos
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Construimos la URL usando caracteres separados para evitar caracteres invisibles
# El error de posición 28 es el punto después de "jack33eo.mp7786j2ncsusov57"
url_base = "https://jack33eo.mp7786j2ncsusov57"
url_sufijo = "general.ru/es/football/conmebol-copa-libertadores-4375787/rosario-central-vs-universidad-central-de-venezuela.html?icg=RVM&ilang=es"
URL = url_base + url_sufijo

async def main():
    bot = Bot(token=TOKEN)
    try:
        # User-Agent para evitar bloqueo
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(URL, headers=headers)
        
        if response.status_code == 200:
            await bot.send_message(chat_id=CHAT_ID, text="✅ ¡Conexión exitosa y limpia!")
        else:
            print(f"Error HTTP: {response.status_code}")
            
    except Exception as e:
        # Imprimimos el error crudo para ver si hay algo más
        print(f"Error de tipo: {type(e)}")
        print(f"Error detallado: {e}")

if __name__ == "__main__":
    asyncio.run(main())
