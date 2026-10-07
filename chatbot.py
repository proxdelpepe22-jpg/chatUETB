# chatbot.py

import re

from memoria import Memoria
from respuestas import (
    saludo,
    despedida,
    agradecimiento,
    respuesta_desconocida,
    respuesta_ayuda,
    respuesta_sobre_mi
)

from funciones import (
    obtener_hora,
    obtener_fecha,
    obtener_dia,
    calculadora_basica
)

from clima import obtener_clima


class Chatbot:

    def __init__(self):
        self.memoria = Memoria()
        self.activo = True

    def limpiar_texto(self, texto):
        """Limpia y normaliza el mensaje."""
        texto = texto.lower().strip()

        # Eliminar signos innecesarios
        texto = re.sub(r"[¿?!¡]", "", texto)

        return texto

    def detectar_nombre(self, texto):
        """
        Detecta frases como:
        - Me llamo Dome
        - Mi nombre es Dome
        - Soy Dome
        """

        patrones = [
            r"me llamo\s+([a-záéíóúñ]+)",
            r"mi nombre es\s+([a-záéíóúñ]+)",
            r"soy\s+([a-záéíóúñ]+)"
        ]

        for patron in patrones:
            resultado = re.search(patron, texto, re.IGNORECASE)

            if resultado:
                nombre = resultado.group(1).capitalize()

                # Evitar guardar palabras que no sean nombres
                palabras_no_validas = [
                    "chatUETB",
                    "estudiante"
                ]

                if nombre.lower() not in [
                    palabra.lower() for palabra in palabras_no_validas
                ]:
                    return nombre

        return None

    def es_saludo(self, texto):
        saludos = [
            "hola",
            "holaa",
            "holaaa",
            "buenas",
            "buenos dias",
            "buenas tardes",
            "buenas noches",
            "hey",
            "hello"
        ]

        return any(texto == saludo_texto for saludo_texto in saludos)

    def es_despedida(self, texto):
        despedidas = [
            "adios",
            "chao",
            "chau",
            "hasta luego",
            "hasta pronto",
            "nos vemos",
            "me voy",
            "salir",
            "cerrar"
        ]

        return any(palabra in texto for palabra in despedidas)

    def es_agradecimiento(self, texto):
        palabras = [
            "gracias",
            "muchas gracias",
            "te agradezco"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_hora(self, texto):
        palabras = [
            "que hora",
            "qué hora",
            "hora actual",
            "dime la hora",
            "hora tenemos"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_fecha(self, texto):
        palabras = [
            "que fecha",
            "qué fecha",
            "fecha actual",
            "fecha de hoy",
            "hoy es"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_dia(self, texto):
        palabras = [
            "que dia",
            "qué dia",
            "qué día",
            "que día",
            "dia de hoy",
            "día de hoy"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_clima(self, texto):
        palabras = [
            "clima",
            "tiempo",
            "temperatura",
            "lluvia",
            "llueve",
            "calor",
            "frio",
            "frío"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_ayuda(self, texto):
        palabras = [
            "ayuda",
            "que puedes hacer",
            "qué puedes hacer",
            "comandos",
            "funciones"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_sobre_mi(self, texto):
        palabras = [
            "quien eres",
            "quién eres",
            "que eres",
            "qué eres",
            "como funcionas",
            "cómo funcionas",
            "quien te creo",
            "quién te creó"
        ]

        return any(palabra in texto for palabra in palabras)

    def es_nombre_usuario(self, texto):
        preguntas = [
            "como me llamo",
            "cómo me llamo",
            "cual es mi nombre",
            "cuál es mi nombre",
            "recuerdas mi nombre"
        ]

        return any(pregunta in texto for pregunta in preguntas)

    def obtener_nombre_ciudad(self, texto):
        """
        Busca expresiones como:
        clima en Machala
        tiempo en Quito
        temperatura en Guayaquil
        """

        patrones = [
            r"clima en\s+(.+)",
            r"tiempo en\s+(.+)",
            r"temperatura en\s+(.+)",
            r"clima de\s+(.+)",
            r"tiempo de\s+(.+)"
        ]

        for patron in patrones:
            resultado = re.search(
                patron,
                texto,
                re.IGNORECASE
            )

            if resultado:
                ciudad = resultado.group(1).strip()
                return ciudad

        return None

    def conocimiento_general(self, texto):

        conocimientos = {
            "capital de ecuador": "🇪🇨 La capital de Ecuador es Quito.",
            "capital del ecuador": "🇪🇨 La capital de Ecuador es Quito.",
            "planeta mas grande": "🪐 El planeta más grande del sistema solar es Júpiter.",
            "planeta más grande": "🪐 El planeta más grande del sistema solar es Júpiter.",
            "cuantos continentes": "🌎 Generalmente se consideran siete continentes.",
            "cuántos continentes": "🌎 Generalmente se consideran siete continentes.",
            "idioma de ecuador": "🇪🇨 El idioma oficial de Ecuador es el castellano o español.",
            "idioma oficial de ecuador": "🇪🇨 El idioma oficial de Ecuador es el castellano o español.",
            "capital de peru": "🇵🇪 La capital de Perú es Lima.",
            "capital de colombia": "🇨🇴 La capital de Colombia es Bogotá.",
            "capital de españa": "🇪🇸 La capital de España es Madrid."
        }

        for pregunta, respuesta in conocimientos.items():

            if pregunta in texto:
                return respuesta

        return None

    def procesar_mensaje(self, mensaje):

        if not mensaje or not mensaje.strip():
            return "✍️ Escribe algo para que pueda ayudarte."

        texto_original = mensaje.strip()
        texto = self.limpiar_texto(texto_original)

        # --------------------------------
        # COMANDOS
        # --------------------------------

        if texto == "/salir":
            self.activo = False
            return despedida()

        if texto == "/ayuda":
            return respuesta_ayuda()

        if texto == "/hora":
            return obtener_hora()

        if texto == "/fecha":
            return obtener_fecha()

        if texto == "/clima":
            return obtener_clima()

        # --------------------------------
        # NOMBRE
        # --------------------------------

        nombre = self.detectar_nombre(texto)

        if nombre:
            self.memoria.guardar("nombre", nombre)

            return (
                f"¡Mucho gusto, {nombre}! 😊\n"
                f"Recordaré tu nombre mientras chatUETB esté abierto."
            )

        if self.es_nombre_usuario(texto):

            nombre = self.memoria.obtener("nombre")

            if nombre:
                return f"👤 Tu nombre es {nombre}."

            return (
                "🤔 Todavía no sé tu nombre. "
                "Puedes decirme: 'Me llamo Dome'."
            )

        # --------------------------------
        # SALUDO
        # --------------------------------

        if self.es_saludo(texto):

            nombre = self.memoria.obtener("nombre")

            if nombre:
                return f"¡Hola, {nombre}! 👋 ¿En qué puedo ayudarte?"

            return saludo()

        # --------------------------------
        # DESPEDIDA
        # --------------------------------

        if self.es_despedida(texto):
            self.activo = False
            return despedida()

        # --------------------------------
        # AGRADECIMIENTO
        # --------------------------------

        if self.es_agradecimiento(texto):
            return agradecimiento()

        # --------------------------------
        # HORA
        # --------------------------------

        if self.es_hora(texto):
            return obtener_hora()

        # --------------------------------
        # FECHA
        # --------------------------------

        if self.es_fecha(texto):
            return obtener_fecha()

        # --------------------------------
        # DÍA
        # --------------------------------

        if self.es_dia(texto):
            return obtener_dia()

        # --------------------------------
        # CLIMA
        # --------------------------------

        if self.es_clima(texto):

            ciudad = self.obtener_nombre_ciudad(texto)

            return obtener_clima(ciudad)

        # --------------------------------
        # AYUDA
        # --------------------------------

        if self.es_ayuda(texto):
            return respuesta_ayuda()

        # --------------------------------
        # SOBRE CHATUETB
        # --------------------------------

        if self.es_sobre_mi(texto):
            return respuesta_sobre_mi()

        # --------------------------------
        # CALCULADORA
        # --------------------------------

        if texto.startswith("calcula "):
            operacion = texto.replace("calcula ", "", 1)
            return calculadora_basica(operacion)

        # --------------------------------
        # CONOCIMIENTO GENERAL
        # --------------------------------

        respuesta = self.conocimiento_general(texto)

        if respuesta:
            return respuesta

        # --------------------------------
        # NO RECONOCIDO
        # --------------------------------

        return respuesta_desconocida()