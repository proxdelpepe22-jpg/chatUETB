# clima.py

import requests

from configuracion import OPENWEATHER_API_KEY, CIUDAD_DEFAULT


URL_CLIMA = "https://api.openweathermap.org/data/2.5/weather"


def obtener_clima(ciudad=None):
    """
    Consulta el clima actual utilizando OpenWeather.
    """

    if not OPENWEATHER_API_KEY:
        return (
            "⚠️ La función del clima todavía no está configurada.\n\n"
            "Debes colocar tu API Key de OpenWeather en el archivo .env."
        )

    if not ciudad:
        ciudad = CIUDAD_DEFAULT

    parametros = {
        "q": ciudad,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        respuesta = requests.get(
            URL_CLIMA,
            params=parametros,
            timeout=10
        )

        if respuesta.status_code == 401:
            return "⚠️ La API Key del clima no es válida."

        if respuesta.status_code == 404:
            return f"⚠️ No encontré la ciudad: {ciudad}."

        if respuesta.status_code != 200:
            return "⚠️ El servicio meteorológico no está disponible."

        datos = respuesta.json()

        nombre = datos.get("name", ciudad)
        temperatura = datos["main"]["temp"]
        sensacion = datos["main"]["feels_like"]
        humedad = datos["main"]["humidity"]

        descripcion = datos["weather"][0]["description"]

        descripcion = descripcion.capitalize()

        return (
            f"🌤️ Clima en {nombre}\n\n"
            f"🌡️ Temperatura: {temperatura:.1f} °C\n"
            f"🌡️ Sensación térmica: {sensacion:.1f} °C\n"
            f"☁️ Condición: {descripcion}\n"
            f"💧 Humedad: {humedad}%"
        )

    except requests.exceptions.Timeout:
        return (
            "⚠️ La consulta del clima tardó demasiado. "
            "Intenta nuevamente."
        )

    except requests.exceptions.ConnectionError:
        return (
            "⚠️ No hay conexión a Internet. "
            "No puedo consultar el clima."
        )

    except Exception:
        return (
            "⚠️ Ocurrió un error al consultar el clima."
        )