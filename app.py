import os
import streamlit as st

# ==========================================================
# CONFIGURAR LA API DE OPENWEATHER
# ==========================================================

try:
    if "OPENWEATHER_API_KEY" in st.secrets:
        os.environ["OPENWEATHER_API_KEY"] = st.secrets["OPENWEATHER_API_KEY"]
except Exception:
    pass

# Importamos nuestro chatbot
from chatbot import Chatbot


# ==========================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================================

st.set_page_config(
    page_title="chatUETB",
    page_icon="🤖",
    layout="centered"
)


# ==========================================================
# TÍTULO
# ==========================================================

st.title("🤖 chatUETB")
st.caption("Tu asistente virtual educativo")


# ==========================================================
# INICIALIZAR EL CHATBOT
# ==========================================================

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "¡Hola! 👋 Soy chatUETB. "
                "Puedes preguntarme la hora, fecha, clima, "
                "hacer cálculos o conocer mis funciones."
            )
        }
    ]


# ==========================================================
# BARRA LATERAL
# ==========================================================

with st.sidebar:
    st.header("chatUETB")

    st.write("### Funciones")

    st.write("🕐 Consultar la hora")
    st.write("📅 Consultar la fecha")
    st.write("🌤️ Consultar el clima")
    st.write("🧮 Realizar cálculos")
    st.write("💬 Conversar")
    st.write("❓ Consultar ayuda")

    st.divider()

    if st.button("🔄 Nuevo chat", use_container_width=True):
        st.session_state.chatbot = Chatbot()
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "¡Hola nuevamente! 👋 ¿En qué puedo ayudarte?"
            }
        ]
        st.rerun()


# ==========================================================
# MOSTRAR HISTORIAL DEL CHAT
# ==========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])


# ==========================================================
# ENTRADA DEL USUARIO
# ==========================================================

if st.session_state.chatbot.activo:

    prompt = st.chat_input("Escribe tu mensaje...")

    if prompt:

        # Mostrar mensaje del usuario
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.write(prompt)

        # Procesar mensaje con nuestro chatbot
        respuesta = st.session_state.chatbot.procesar_mensaje(prompt)

        # Guardar respuesta
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": respuesta
            }
        )

        # Mostrar respuesta
        with st.chat_message("assistant"):
            st.write(respuesta)

        # Si el chatbot fue desactivado con /salir
        if not st.session_state.chatbot.activo:
            st.info("El chat ha finalizado. Pulsa «Nuevo chat» para comenzar otra conversación.")

else:

    st.info(
        "El chat está cerrado. Pulsa «Nuevo chat» en la barra lateral para comenzar."
    )