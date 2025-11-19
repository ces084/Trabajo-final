from mensaje import Mensaje

class ColaUrgentes:
    def __init__(self):
        self.urgentes = []

    def marcar_urgente(self, mensaje: Mensaje):
        if mensaje not in self.urgentes:
            self.urgentes.append(mensaje)
            print("Mensaje marcado como URGENTE")

    def siguiente(self):
        if self.urgentes:
            return self.urgentes.pop(0)
        return None