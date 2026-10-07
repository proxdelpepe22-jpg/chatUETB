import os
from dotenv import load_dotenv

load_dotenv()

NOMBRE_CHATBOT = "chatUETB"

ZONA_HORARIA = "America/Guayaquil"

# Obtener la API Key de Streamlit o del archivo .env
try:
    import streamlit as st

    if "OPENWEATHER_API_KEY" in st.secrets:
        OPENWEATHER_API_KEY = st.secrets["OPENWEATHER_API_KEY"]
    else:
        OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

except Exception:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

CIUDAD_DEFAULT = "Machala"

# Configuración de la interfaz
VENTANA_TITULO = "chatUETB - Asistente Virtual"
ANCHO_VENTANA = 850
ALTO_VENTANA = 600