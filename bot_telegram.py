import os
import requests
from telegram import Bot
import asyncio
from bs4 import BeautifulSoup

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Lista de webs a monitorear
WEBS = [
    "https://futbol-libre.su/",
    "https://golxu.com/",
    "https://ppvtv.top/"
]

async def main():
    bot = Bot(token=TOKEN)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://www.google.com/'
    }
    
    mensaje_final = "⚽ **Cartelera Deportiva Detectada:**\n\n"
    encontrados = 0

    for url in WEBS:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                # Buscamos enlaces que contengan partidos (patrón genérico)
                links = soup.find_all('a', href=True)
                
                for a in links[:3]: # Tomamos los 3 primeros de cada web
                    texto = a.get_text(strip=True)
                    if len(texto) > 15: # Filtramos menús cortos
                        link = a['href']
                        if not link.startswith('http'): link = url.rstrip('/') + link
                        mensaje_final += f"🔹 {texto}\n🔗 {link}\n\n"
                        encontrados += 1
        except:
            continue # Si una web falla, intentamos la siguiente sin detenernos

    if encontrados > 0:
        await bot.send_message(chat_id=CHAT_ID, text=mensaje_final, parse_mode='Markdown')
    else:
        await bot.send_message(chat_id=CHAT_ID, text="No pude extraer información. Las webs tienen sistemas de seguridad activos.")

if __name__ == "__main__":
    asyncio.run(main())
