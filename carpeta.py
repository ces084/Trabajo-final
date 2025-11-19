from typing import List, Optional
from mensaje import Mensaje

class Carpeta:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._mensajes: List[Mensaje] = []
        self._subcarpetas: List[Carpeta] = []  

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def mensajes(self) -> List[Mensaje]:
        return self._mensajes

    @property
    def subcarpetas(self) -> List['Carpeta']:
        return self._subcarpetas

    def agregar_subcarpeta(self, subcarpeta: 'Carpeta') -> None:
        self._subcarpetas.append(subcarpeta)

    def guardar_mensaje(self, mensaje: Mensaje) -> None:
        self._mensajes.append(mensaje)

    def remover_mensaje(self, mensaje: Mensaje) -> None:
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)

    # Búsqueda recursiva de carpeta por nombre
    def buscar_carpeta(self, nombre: str) -> Optional['Carpeta']:
        if self._nombre == nombre:
            return self
        for sub in self._subcarpetas:
            encontrada = sub.buscar_carpeta(nombre)
            if encontrada:
                return encontrada
        return None

    # Búsqueda recursiva de mensajes por asunto
    def buscar_mensajes_por_asunto(self, asunto: str) -> List[str]:
        resultados = []
        for m in self._mensajes:
            if asunto.lower() in m.titulo.lower():
                resultados.append(str(m))
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensajes_por_asunto(asunto))
        return resultados

    # Búsqueda recursiva de mensajes por remitente
    def buscar_mensajes_por_remitente(self, remitente_correo: str) -> List[str]:
        resultados = []
        for m in self._mensajes:
            if m.remitente.correo.lower() == remitente_correo.lower():
                resultados.append(str(m))
        for sub in self._subcarpetas:
            resultados.extend(sub.buscar_mensajes_por_remitente(remitente_correo))
        return resultados

    def __str__(self) -> str:
        return f"Carpeta {self._nombre} ({len(self._mensajes)} mensajes, {len(self._subcarpetas)} subcarpetas)"