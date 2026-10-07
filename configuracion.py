# configuracion.py

import os
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

# Nombre del chatbot
NOMBRE_CHATBOT = "chatUETB"

# Zona horaria de Ecuador
ZONA_HORARIA = "America/Guayaquil"

# API del clima
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Ciudad predeterminada
CIUDAD_DEFAULT = "Machala"

# Configuración de la interfaz
VENTANA_TITULO = "chatUETB - Asistente Virtual"
ANCHO_VENTANA = 850
ALTO_VENTANA = 600