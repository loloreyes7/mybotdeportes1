import os
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

# Obtiene los secretos configurados en GitHub
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://jack33eo.mp7786j2ncsusov57general.ru/es/football/conmebol-copa-libertadores-4375787/rosario-central-vs-universidad-central-de-venezuela.html?icg=RVM&ilang=es"

async def main():
    if not TOKEN or not CHAT_ID:
        print("Error: Los secretos no están bien configurados.")
        return

    bot = Bot(token=TOKEN)
    
    try:
        # Descarga la web
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrae el título de la página como prueba
        titulo = soup.find('title').text.strip()
        
        # Envía el mensaje a Telegram
        mensaje = f"✅ ¡Bot funcionando!\nLeyendo: {titulo}\n🔗 {URL}"
        await bot.send_message(chat_id=CHAT_ID, text=mensaje)
        print("Mensaje enviado con éxito.")
            
    except Exception as e:
        print(f"Error al ejecutar: {e}")

if __name__ == "__main__":
    asyncio.run(main())
