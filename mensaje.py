class Mensaje:
    def __init__(self, remitente, destinatario, titulo: str, contenido: str):
        self._remitente = remitente
        self._destinatario = destinatario
        self._titulo = titulo
        self._contenido = contenido

    @property
    def remitente(self):
        return self._remitente

    @property
    def destinatario(self):
        return self._destinatario

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def contenido(self) -> str:
        return self._contenido

    def __str__(self) -> str:
        return f"[{self._titulo}] De: {self._remitente.correo} Para: {self._destinatario.correo} - {self._contenido}"