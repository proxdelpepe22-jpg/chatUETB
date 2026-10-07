# memoria.py

class Memoria:
    def __init__(self):
        self.datos = {}

    def guardar(self, clave, valor):
        """Guarda información en la memoria."""
        self.datos[clave] = valor

    def obtener(self, clave, valor_predeterminado=None):
        """Obtiene información almacenada."""
        return self.datos.get(clave, valor_predeterminado)

    def eliminar(self, clave):
        """Elimina información de la memoria."""
        if clave in self.datos:
            del self.datos[clave]

    def limpiar(self):
        """Borra toda la memoria."""
        self.datos.clear()

    def tiene(self, clave):
        """Comprueba si existe una información."""
        return clave in self.datos