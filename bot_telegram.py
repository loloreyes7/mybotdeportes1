import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://www.fctv33hd.skin/es"

async def main():
    async with async_playwright() as p:
        # Lanzamos con un perfil que parece más humano
        browser = await p.chromium.launch()
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        page = await context.new_page()
        
        try:
            await page.goto(URL, wait_until="domcontentloaded", timeout=60000)
            
            # Esperamos 30 segundos en lugar de 10
            await page.wait_for_selector(".cp-link", timeout=30000)
            
            eventos = await page.eval_on_selector_all(".cp-link", """elements => elements.map(e => ({
                texto: e.innerText,
                link: e.href
            }))""")
            
            if not eventos:
                raise Exception("No se encontraron elementos con clase .cp-link")

            mensaje = "📅 **Agenda Deportiva (Detectada):**\n\n"
            for e in eventos[:6]:
                mensaje += f"🔹 {e['texto']}\n🔗 {e['link']}\n\n"
                
            bot = Bot(token=TOKEN)
            await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
            
        except Exception as e:
            print(f"Error extrayendo datos: {e}")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
