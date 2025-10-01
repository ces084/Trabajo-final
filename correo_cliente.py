from typing import List

class Usuario:
    def __init__(self, correo: str, nombre: str):
        self._correo = correo
        self._nombre = nombre
        self._bandejas: List['Carpeta'] = []

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def bandejas(self) -> List['Carpeta']:
        return self._bandejas

    def crear_carpeta(self, carpeta: 'Carpeta') -> None:
        self._bandejas.append(carpeta)

    def __str__(self) -> str:
        return f"{self._nombre} <{self._correo}>"


class Mensaje:
    def __init__(self, remitente: Usuario, destinatario: Usuario, titulo: str, contenido: str):
        self._remitente = remitente
        self._destinatario = destinatario
        self._titulo = titulo
        self._contenido = contenido

    @property
    def remitente(self) -> Usuario:
        return self._remitente

    @property
    def destinatario(self) -> Usuario:
        return self._destinatario

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def contenido(self) -> str:
        return self._contenido

    def __str__(self) -> str:
        return f"[{self._titulo}] De: {self._remitente.correo} Para: {self._destinatario.correo} - {self._contenido}"


class Carpeta:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._mensajes: List[Mensaje] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mensajes(self) -> List[Mensaje]:
        return self._mensajes

    def guardar_mensaje(self, mensaje: Mensaje) -> None:
        self._mensajes.append(mensaje)

    def __str__(self) -> str:
        return f"Bandeja {self._nombre} ({len(self._mensajes)} mensajes)"


class ServidorCorreo:
    def __init__(self):
        self._usuarios: List[Usuario] = []

    @property
    def usuarios(self) -> List[Usuario]:
        return self._usuarios

    def registrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def enviar_mensaje(self, remitente: Usuario, destinatario: Usuario, asunto: str, cuerpo: str) -> None:
        nuevo_mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
        entrada = next((c for c in destinatario.bandejas if c.nombre == "Entrada"), None)
        if not entrada:
            entrada = Carpeta("Entrada")
            destinatario.crear_carpeta(entrada)
        entrada.guardar_mensaje(nuevo_mensaje)

    def recibir_mensajes(self, usuario: Usuario) -> List[str]:
        entrada = next((c for c in usuario.bandejas if c.nombre == "Entrada"), None)
        if entrada:
            return [str(m) for m in entrada.mensajes]
        return []

    def listar_mensajes(self, carpeta: Carpeta) -> List[str]:
        return [str(m) for m in carpeta.mensajes]

    def __str__(self) -> str:
        return f"Servidor con {len(self._usuarios)} usuarios registrados"


# Ejemplo de uso mínimo
if __name__ == "__main__":
    servidor = ServidorCorreo()

    usuario1 = Usuario("ana@mail.com", "Ana")
    usuario2 = Usuario("juan@mail.com", "Juan")

    servidor.registrar_usuario(usuario1)
    servidor.registrar_usuario(usuario2)

    servidor.enviar_mensaje(usuario1, usuario2, "Hola", "¿Cómo estas?")
    servidor.enviar_mensaje(usuario2, usuario1, "Re: Hola", "Todo bien 💫")

    print("Usuarios en servidor:")
    for u in servidor.usuarios:
        print(u)

    print("\nMensajes recibidos por Juan:")
    for m in servidor.recibir_mensajes(usuario2):
        print(m)

    print("\nMensajes recibidos por Ana:")
    for m in servidor.recibir_mensajes(usuario1):
        print(m)