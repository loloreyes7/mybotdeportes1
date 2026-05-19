import os
import requests
from bs4 import BeautifulSoup
from telegram import Bot
import asyncio

# Obtiene las variables de entorno configuradas en GitHub Secrets
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://www.fctv33hd.skin/es"

async def main():
    # Verificación básica
    if not TOKEN or not CHAT_ID:
        print("Error: TOKEN o CHAT_ID no configurados.")
        return

    bot = Bot(token=TOKEN)
    try:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ajusta estos selectores según la estructura real de la web
        # NOTA: '.evento-clase' es un ejemplo, asegúrate de que coincida con la clase CSS de la web
        partidos = soup.select('.evento-clase') 
        
        if not partidos:
            print("No se encontraron partidos. Revisa los selectores.")
            return

        for p in partidos:
            # Aquí procesarías el texto y los enlaces
            msg = f"⚽ Partido: {p.text.strip()}\n🔗 {URL}"
            await bot.send_message(chat_id=CHAT_ID, text=msg)
            
    except Exception as e:
        print(f"Error al ejecutar: {e}")

if __name__ == "__main__":
    asyncio.run(main())