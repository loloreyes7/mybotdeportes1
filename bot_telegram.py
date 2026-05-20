import os
import requests
from telegram import Bot
import asyncio
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://jack33eo.mp7786j2ncsusov57general.ru/es/football/conmebol-copa-libertadores-4375787/rosario-central-vs-universidad-central-de-venezuela.html?icg=RVM&ilang=es"

async def main():
    bot = Bot(token=TOKEN)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos los equipos usando los selectores que encontraste
        home = soup.select_one('.home-team')
        away = soup.select_one('.away-team')

        if home and away:
            nombre_home = home.get_text(strip=True)
            nombre_away = away.get_text(strip=True)
            mensaje = f"⚽ **Partido detectado:**\n{nombre_home} vs {nombre_away}"
            await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
        else:
            await bot.send_message(chat_id=CHAT_ID, text="No pude encontrar los nombres de los equipos. El diseño de la web podría haber cambiado.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
