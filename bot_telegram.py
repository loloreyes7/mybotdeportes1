import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://www.fctv33hd.skin/es"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Entramos en la web y esperamos a que cargue el contenido
        await page.goto(URL, wait_until="networkidle")
        
        # Esperamos a que los elementos del partido estén visibles
        try:
            await page.wait_for_selector(".cp-link", timeout=10000)
            
            # Extraemos texto y links
            eventos = await page.eval_on_selector_all(".cp-link", """elements => elements.map(e => ({
                texto: e.innerText,
                link: e.href
            }))""")
            
            mensaje = "📅 **Agenda Deportiva (Actualizada):**\n\n"
            for e in eventos[:6]:
                mensaje += f"🔹 {e['texto']}\n🔗 {e['link']}\n\n"
                
            bot = Bot(token=TOKEN)
            await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
            
        except Exception as e:
            print(f"Error extrayendo datos: {e}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
