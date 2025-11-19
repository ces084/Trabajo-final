from mensaje import Mensaje
from carpeta import Carpeta

class Filtro:
    def __init__(self):
        
        self.reglas = {}

    def agregar_regla(self, palabra: str, carpeta_destino: str):
        self.reglas[palabra.lower()] = carpeta_destino
        print(f"Regla: si contiene '{palabra}' → va a '{carpeta_destino}'")

    def aplicar(self, mensaje: Mensaje, carpetas_raiz):
        contenido = (mensaje.titulo + " " + mensaje.contenido).lower()
        for palabra, carpeta_nombre in self.reglas.items():
            if palabra in contenido:
                # Buscar carpeta destino
                destino = None
                for raiz in carpetas_raiz:
                    destino = raiz.buscar_carpeta(carpeta_nombre)
                    if destino:
                        break
                if destino:
                    destino.guardar_mensaje(mensaje)
                    return carpeta_nombre
        return None 