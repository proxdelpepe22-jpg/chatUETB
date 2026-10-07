# funciones.py

from datetime import datetime
from zoneinfo import ZoneInfo

from configuracion import ZONA_HORARIA


DIAS = [
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo"
]

MESES = [
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre"
]


def obtener_fecha_hora():
    """Obtiene la fecha y hora actual de Ecuador."""
    try:
        zona = ZoneInfo(ZONA_HORARIA)
        return datetime.now(zona)
    except Exception:
        return datetime.now()


def obtener_hora():
    """Devuelve la hora actual."""
    ahora = obtener_fecha_hora()

    hora = ahora.strftime("%I")
    minutos = ahora.strftime("%M")
    periodo = ahora.strftime("%p")

    if periodo == "AM":
        periodo = "a. m."
    else:
        periodo = "p. m."

    return f"🕐 Son las {hora}:{minutos} {periodo}."


def obtener_fecha():
    """Devuelve la fecha actual en español."""
    ahora = obtener_fecha_hora()

    dia_semana = DIAS[ahora.weekday()]
    dia = ahora.day
    mes = MESES[ahora.month - 1]
    año = ahora.year

    return f"📅 Hoy es {dia_semana} {dia} de {mes} de {año}."


def obtener_dia():
    """Devuelve solamente el día de la semana."""
    ahora = obtener_fecha_hora()
    return f"Hoy es {DIAS[ahora.weekday()]}."


def calculadora_basica(operacion):
    """
    Calculadora sencilla.
    Esta función no ejecuta código introducido por el usuario.
    """

    try:
        operacion = operacion.strip()

        # Permitimos únicamente números y operadores básicos
        caracteres_permitidos = "0123456789+-*/(). "

        if not all(c in caracteres_permitidos for c in operacion):
            return "⚠️ Solo puedo realizar operaciones matemáticas básicas."

        resultado = eval(operacion, {"__builtins__": {}}, {})

        return f"🧮 Resultado: {resultado}"

    except ZeroDivisionError:
        return "⚠️ No se puede dividir para cero."

    except Exception:
        return "⚠️ No pude realizar esa operación."