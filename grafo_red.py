from collections import deque

class RedServidores:
    def __init__(self):
        self.servidores = {}  # "servidor1": [servidor2, servidor3]

    def conectar(self, s1: str, s2: str):
        if s1 not in self.servidores:
            self.servidores[s1] = []
        if s2 not in self.servidores:
            self.servidores[s2] = []
        self.servidores[s1].append(s2)
        self.servidores[s2].append(s1)
        print(f"Conectado {s1} ↔ {s2}")

    def enviar_con_ruta(self, origen: str, destino: str, mensaje: str):
        if origen not in self.servidores or destino not in self.servidores:
            return None

        cola = deque([[origen]])
        visitados = {origen}

        while cola:
            ruta = cola.popleft()
            actual = ruta[-1]
            if actual == destino:
                print(f"Ruta encontrada: {' → '.join(ruta)}")
                print(f"Mensaje enviado: {mensaje}")
                return ruta

            for vecino in self.servidores[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(ruta + [vecino])
        print("No hay ruta")
        return None