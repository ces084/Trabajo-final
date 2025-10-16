from typing import List
from carpeta import Carpeta

class Usuario:
    def __init__(self, correo: str, nombre: str):
        self._correo = correo
        self._nombre = nombre
        self._bandejas: List[Carpeta] = []  # Ahora son carpetas raíz, que pueden tener subcarpetas

    @property
    def correo(self) -> str:
        return self._correo

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def bandejas(self) -> List[Carpeta]:
        return self._bandejas

    def crear_carpeta(self, carpeta: Carpeta) -> None:
        self._bandejas.append(carpeta)

    def __str__(self) -> str:
        return f"{self._nombre} <{self._correo}>"