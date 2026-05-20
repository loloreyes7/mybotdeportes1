import os
import requests
from telegram import Bot
import asyncio
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://jack33eo.mp7786j2ncsusov57general.ru/es/basketball.html" # Ajustado a baloncesto

async def main():
    bot = Bot(token=TOKEN)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos los bloques que contienen la información (usando tu selector)
        # Buscamos elementos que tengan la clase 'cp-link'
        partidos = soup.select('.cp-link')
        
        if not partidos:
            await bot.send_message(chat_id=CHAT_ID, text="No encontré partidos activos en este momento.")
            return

        mensaje = "🏀 **Partidos de Baloncesto en Vivo:**\n\n"
        
        for p in partidos[:5]: # Los 5 primeros
            texto = p.get_text(strip=True)
            link_tag = p.find_parent('a') # Buscamos el enlace padre
            link = link_tag['href'] if link_tag and link_tag.has_attr('href') else "Sin enlace"
            
            # Aseguramos que el enlace tenga el dominio completo
            if link.startswith('/'):
                link = "https://jack33eo.mp7786j2ncsusov57general.ru" + link
            
            mensaje += f"🔹 {texto}\n🔗 {link}\n\n"

        await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
            
    except Exception as e:
        print(f"Error técnico: {e}")

if __name__ == "__main__":
    asyncio.run(main())
