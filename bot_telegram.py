import os
import requests
from telegram import Bot
from bs4 import BeautifulSoup
import asyncio

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://futbol-libre.su/"

async def main():
    bot = Bot(token=TOKEN)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    
    try:
        response = requests.get(URL, headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Ejemplo: buscamos enlaces de partidos
        links = soup.find_all('a', href=True)
        mensaje = "⚽ **Cartelera detectada:**\n\n"
        
        for a in links[:5]:
            texto = a.get_text(strip=True)
            if len(texto) > 10:
                mensaje += f"🔹 {texto}\n"
        
        await bot.send_message(chat_id=CHAT_ID, text=mensaje)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
