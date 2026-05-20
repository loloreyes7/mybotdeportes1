import os
import requests
from telegram import Bot
import asyncio

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
# API oficial del SAIH Guadalquivir para puntos de control
API_URL = "https://www.chguadalquivir.es/saih-web/api/estaciones"

async def main():
    bot = Bot(token=TOKEN)
    try:
        # Consultamos los datos reales
        response = requests.get(API_URL, timeout=10)
        datos = response.json()
        
        mensaje = "🌊 **Estado de los Ríos - SAIH Guadalquivir:**\n\n"
        
        # Filtramos los datos de los 5 puntos de control principales
        for estacion in datos[:5]:
            nombre = estacion.get('nombre', 'Desconocido')
            caudal = estacion.get('caudal', 'N/A')
            nivel = estacion.get('nivel', 'N/A')
            mensaje += f"📍 {nombre}\n   💧 Caudal: {caudal} m³/s\n   📏 Nivel: {nivel} m\n\n"
        
        await bot.send_message(chat_id=CHAT_ID, text=mensaje, parse_mode='Markdown')
            
    except Exception as e:
        print(f"Error al obtener datos: {e}")

if __name__ == "__main__":
    asyncio.run(main())
