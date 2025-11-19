from typing import List, Optional
from usuario import Usuario
from mensaje import Mensaje
from carpeta import Carpeta
from filtro import Filtro
from cola_urgentes import ColaUrgentes
from grafo_red import RedServidores

class ServidorCorreo:
    def __init__(self):
        self._usuarios: List[Usuario] = []
        self.filtro = Filtro()           
        self.cola_urgentes = ColaUrgentes() 
        self.red = RedServidores()       
        self.nombre = "ServidorLocal"   

    @property
    def usuarios(self) -> List[Usuario]:
        return self._usuarios

    def registrar_usuario(self, usuario: Usuario) -> None:
        self._usuarios.append(usuario)

    def enviar_mensaje(self, remitente: Usuario, destinatario: Usuario, asunto: str, cuerpo: str) -> None:
        nuevo_mensaje = Mensaje(remitente, destinatario, asunto, cuerpo)
        entrada = self._obtener_o_crear_entrada(destinatario)
        entrada.guardar_mensaje(nuevo_mensaje)

    def _obtener_o_crear_entrada(self, usuario: Usuario) -> Carpeta:
        for c in usuario.bandejas:
            entrada = c.buscar_carpeta("Entrada")
            if entrada:
                return entrada
        entrada = Carpeta("Entrada")
        usuario.crear_carpeta(entrada)
        return entrada

    def recibir_mensajes(self, usuario: Usuario) -> List[str]:
        entrada = self._obtener_o_crear_entrada(usuario)
        return [str(m) for m in entrada.mensajes]

    def listar_mensajes(self, carpeta: Carpeta) -> List[str]:
        return [str(m) for m in carpeta.mensajes]

    # Mover mensaje entre carpetas (busca recursivamente)
    def mover_mensaje(self, usuario: Usuario, origen_nombre: str, destino_nombre: str, indice_mensaje: int) -> bool:
        origen = self._buscar_carpeta_en_usuario(usuario, origen_nombre)
        destino = self._buscar_carpeta_en_usuario(usuario, destino_nombre)
        if origen and destino and 0 <= indice_mensaje < len(origen.mensajes):
            mensaje = origen.mensajes[indice_mensaje]
            origen.remover_mensaje(mensaje)
            destino.guardar_mensaje(mensaje)
            return True
        return False

    # Búsqueda por asunto en todas las carpetas del usuario
    def buscar_mensajes_por_asunto(self, usuario: Usuario, asunto: str) -> List[str]:
        resultados = []
        for c in usuario.bandejas:
            resultados.extend(c.buscar_mensajes_por_asunto(asunto))
        return resultados

    # Búsqueda por remitente en todas las carpetas del usuario
    def buscar_mensajes_por_remitente(self, usuario: Usuario, remitente_correo: str) -> List[str]:
        resultados = []
        for c in usuario.bandejas:
            resultados.extend(c.buscar_mensajes_por_remitente(remitente_correo))
        return resultados

    def _buscar_carpeta_en_usuario(self, usuario: Usuario, nombre: str) -> Optional[Carpeta]:
        for c in usuario.bandejas:
            encontrada = c.buscar_carpeta(nombre)
            if encontrada:
                return encontrada
        return None

    def __str__(self) -> str:
        return f"Servidor con {len(self._usuarios)} usuarios registrados"