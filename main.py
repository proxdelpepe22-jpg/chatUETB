# main.py

import tkinter as tk
from tkinter import scrolledtext, messagebox

from chatbot import Chatbot
from configuracion import (
    NOMBRE_CHATBOT,
    VENTANA_TITULO,
    ANCHO_VENTANA,
    ALTO_VENTANA
)


class ChatUETBApp:

    def __init__(self, root):

        self.root = root
        self.chatbot = Chatbot()

        # --------------------------------
        # CONFIGURACIÓN DE LA VENTANA
        # --------------------------------

        self.root.title(VENTANA_TITULO)
        self.root.geometry(
            f"{ANCHO_VENTANA}x{ALTO_VENTANA}"
        )

        self.root.minsize(650, 450)

        # --------------------------------
        # ENCABEZADO
        # --------------------------------

        encabezado = tk.Frame(
            self.root,
            bg="#6C5CE7",
            height=70
        )

        encabezado.pack(
            fill="x"
        )

        titulo = tk.Label(
            encabezado,
            text="🤖 chatUETB",
            font=("Arial", 22, "bold"),
            bg="#6C5CE7",
            fg="white"
        )

        titulo.pack(
            pady=(10, 0)
        )

        subtitulo = tk.Label(
            encabezado,
            text="Tu pequeño asistente virtual",
            font=("Arial", 10),
            bg="#6C5CE7",
            fg="white"
        )

        subtitulo.pack()

        # --------------------------------
        # ÁREA DEL CHAT
        # --------------------------------

        self.area_chat = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Arial", 11),
            state=tk.DISABLED,
            bg="#F8F7FC",
            fg="#222222",
            padx=15,
            pady=15
        )

        self.area_chat.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=(15, 5)
        )

        # --------------------------------
        # ÁREA INFERIOR
        # --------------------------------

        frame_entrada = tk.Frame(
            self.root,
            bg="#FFFFFF"
        )

        frame_entrada.pack(
            fill="x",
            padx=15,
            pady=10
        )

        self.entrada = tk.Entry(
            frame_entrada,
            font=("Arial", 12),
            relief=tk.SOLID,
            bd=1
        )

        self.entrada.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=9
        )

        self.entrada.bind(
            "<Return>",
            self.enviar_mensaje
        )

        boton_enviar = tk.Button(
            frame_entrada,
            text="Enviar",
            command=self.enviar_mensaje,
            font=("Arial", 11, "bold"),
            bg="#6C5CE7",
            fg="white",
            activebackground="#5848D8",
            activeforeground="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )

        boton_enviar.pack(
            side="right",
            padx=(10, 0)
        )

        # --------------------------------
        # MENSAJE INICIAL
        # --------------------------------

        self.mostrar_mensaje(
            "chatUETB",
            "¡Hola! 👋 Soy chatUETB.\n\n"
            "Puedo ayudarte con:\n"
            "• Hora\n"
            "• Fecha\n"
            "• Clima\n"
            "• Preguntas sencillas\n"
            "• Tu nombre\n\n"
            "Escribe /ayuda para conocer mis funciones."
        )

        self.entrada.focus()

        # --------------------------------
        # CERRAR VENTANA
        # --------------------------------

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.cerrar_programa
        )

    def mostrar_mensaje(self, remitente, mensaje):

        self.area_chat.config(
            state=tk.NORMAL
        )

        self.area_chat.insert(
            tk.END,
            f"\n{remitente}:\n",
            "remitente"
        )

        self.area_chat.insert(
            tk.END,
            f"{mensaje}\n",
            "mensaje"
        )

        self.area_chat.config(
            state=tk.DISABLED
        )

        self.area_chat.see(
            tk.END
        )

    def enviar_mensaje(self, event=None):

        mensaje = self.entrada.get().strip()

        if not mensaje:
            return

        self.mostrar_mensaje(
            "Tú",
            mensaje
        )

        self.entrada.delete(
            0,
            tk.END
        )

        respuesta = self.chatbot.procesar_mensaje(
            mensaje
        )

        self.mostrar_mensaje(
            NOMBRE_CHATBOT,
            respuesta
        )

        if not self.chatbot.activo:

            self.entrada.config(
                state=tk.DISABLED
            )

    def cerrar_programa(self):

        respuesta = messagebox.askyesno(
            "Salir",
            "¿Quieres cerrar chatUETB?"
        )

        if respuesta:
            self.root.destroy()


def main():

    root = tk.Tk()

    app = ChatUETBApp(
        root
    )

    root.mainloop()


if __name__ == "__main__":
    main()