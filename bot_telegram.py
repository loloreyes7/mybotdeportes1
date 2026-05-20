import os
import requests
from telegram import Bot
import asyncio
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
# Usamos la página principal donde están todos los deportes
URL = "https://www.fctv33hd.skin/es"

async def main():
    bot = Bot(token=TOKEN)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscamos elementos que contienen enlaces a eventos (buscamos patrones comunes de enlaces)
        # En esta web, los eventos suelen estar dentro de etiquetas 'a' con clases específicas
        enlaces = soup.find_all('a', href=True)
        
        mensaje = "📺 **Cartelera Deportiva Global:**\n\n"
        encontrados = []

        for a in enlaces:
            href = a['href']
            # Filtramos enlaces que parecen ser partidos (que contengan 'football', 'basketball', etc)
            if any(deporte in href for deporte in ['football', 'basketball', 'tennis', 'volleyball']):
                texto = a.get_text(strip=True)
                if texto and texto not in encontrados:
                    full_link = "https://www.fctv33hd.skin" + (href if href.startswith('/') else f"/{href}")
                    mensaje += f"🔹 {texto}\n🔗 {full_link}\n\n"
                    encontrados.append(texto)
            
            # Limitamos a 6 eventos para que no sea un mensaje infinito
            if len(encontrados) >= 6:
                break

        if encontrados:
            await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
        else:
            await bot.send_message(chat_id=CHAT_ID, text="No pude detectar eventos en la página principal ahora mismo.")
            
    except Exception as e:
        print(f"Error técnico: {e}")

if __name__ == "__main__":
    asyncio.run(main())
