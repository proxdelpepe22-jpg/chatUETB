# respuestas.py

import random


SALUDOS = [
    "¡Hola! 👋 Soy chatUETB. ¿En qué puedo ayudarte?",
    "¡Hola! 😊 Qué gusto hablar contigo. ¿En qué puedo ayudarte?",
    "¡Hola! 👋 Soy chatUETB, tu asistente virtual.",
    "¡Buenas! 😊 ¿Qué necesitas saber?"
]


DESPEDIDAS = [
    "¡Hasta luego! 👋 Espero poder ayudarte nuevamente.",
    "¡Adiós! 😊 Que tengas un excelente día.",
    "¡Nos vemos! 👋 Gracias por utilizar chatUETB.",
    "¡Hasta pronto! 🤖"
]


AGRADECIMIENTOS = [
    "¡De nada! 😊",
    "¡Con mucho gusto! 👋",
    "No hay de qué. 😊",
    "Estoy aquí para ayudarte. 🤖"
]


RESPUESTAS_DESCONOCIDAS = [
    "🤔 No estoy seguro de haber entendido. Puedes escribir /ayuda para ver lo que puedo hacer.",
    "🤔 Todavía no sé responder esa pregunta. Intenta preguntarme por la hora, fecha o clima.",
    "No tengo una respuesta para eso todavía. 😊 Escribe /ayuda para conocer mis funciones.",
    "Creo que todavía necesito aprender sobre ese tema. 🤖"
]


def saludo():
    return random.choice(SALUDOS)


def despedida():
    return random.choice(DESPEDIDAS)


def agradecimiento():
    return random.choice(AGRADECIMIENTOS)


def respuesta_desconocida():
    return random.choice(RESPUESTAS_DESCONOCIDAS)


def respuesta_ayuda():
    return (
        "🤖 Puedo ayudarte con las siguientes funciones:\n\n"
        "👋 Saludos y despedidas\n"
        "🕐 Hora actual\n"
        "📅 Fecha actual\n"
        "🌤️ Clima\n"
        "👤 Recordar tu nombre\n"
        "🧠 Preguntas sencillas\n"
        "ℹ️ Información sobre mí\n\n"
        "También puedes utilizar estos comandos:\n"
        "/ayuda\n"
        "/hora\n"
        "/fecha\n"
        "/clima\n"
        "/salir"
    )


def respuesta_sobre_mi():
    return (
        "🤖 Soy chatUETB, un pequeño asistente virtual creado "
        "con Python.\n\n"
        "Puedo responder preguntas sencillas, decirte la hora "
        "y fecha, consultar el clima y recordar tu nombre durante "
        "la sesión."
    )