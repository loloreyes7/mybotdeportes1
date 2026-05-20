import os
import requests
from telegram import Bot
import asyncio

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Esta es la dirección donde la web suele buscar los datos de los partidos
# Si esta URL no responde, el bot te avisará.
API_URL = "https://www.fctv33hd.skin/api/events" 

async def main():
    bot = Bot(token=TOKEN)
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        # Intentamos obtener los datos directamente
        response = requests.get(API_URL, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            mensaje = "📅 **Agenda Deportiva de Hoy:**\n\n"
            
            # Aquí asumimos que recibimos una lista de partidos
            for evento in data[:8]: # Los próximos 8 partidos
                hora = evento.get('time', 'Hora no definida')
                nombre = evento.get('name', 'Evento')
                link = evento.get('link', '#')
                mensaje += f"🕒 {hora} - {nombre}\n🔗 {link}\n\n"
            
            await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
        else:
            await bot.send_message(chat_id=CHAT_ID, text="No pude conectar con el servidor de datos. La web podría haber cambiado su estructura.")
            
    except Exception as e:
        print(f"Error: {e}")
        await bot.send_message(chat_id=CHAT_ID, text="Hubo un error técnico al leer la cartelera.")

if __name__ == "__main__":
    asyncio.run(main())
