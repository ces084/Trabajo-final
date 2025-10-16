from usuario import Usuario
from carpeta import Carpeta
from servidor_correo import ServidorCorreo

def mostrar_menu():
    print("\nCorreo Electrónico")
    print("1. Registrar nuevo usuario")
    print("2. Enviar mensaje")
    print("3. Ver mensajes recibidos (bandeja de entrada)")
    print("4. Crear nueva carpeta (raíz)")
    print("5. Crear subcarpeta en una carpeta existente")
    print("6. Ver mensajes en una carpeta")
    print("7. Mover mensaje entre carpetas")
    print("8. Buscar mensajes por asunto (recursivo)")
    print("9. Buscar mensajes por remitente (recursivo)")
    print("10. Salir")
    return input("Seleccione una opción (1-10): ")

def main():
    servidor = ServidorCorreo()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            correo = input("Ingrese el correo del usuario: ")
            nombre = input("Ingrese el nombre del usuario: ")
            usuario = Usuario(correo, nombre)
            servidor.registrar_usuario(usuario)
            print(f"Usuario {nombre} registrado correctamente.")
        
        elif opcion == "2":
            remitente_correo = input("Correo del remitente: ")
            destinatario_correo = input("Correo del destinatario: ")
            asunto = input("Asunto del mensaje: ")
            cuerpo = input("Cuerpo del mensaje: ")
            
            remitente = next((u for u in servidor.usuarios if u.correo == remitente_correo), None)
            destinatario = next((u for u in servidor.usuarios if u.correo == destinatario_correo), None)
            
            if remitente and destinatario:
                servidor.enviar_mensaje(remitente, destinatario, asunto, cuerpo)
                print("Mensaje enviado correctamente.")
            else:
                print("Error: Remitente o destinatario no encontrado.")
        
        elif opcion == "3":
            correo = input("Ingrese el correo del usuario: ")
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                mensajes = servidor.recibir_mensajes(usuario)
                if mensajes:
                    print("\nMensajes en la bandeja de entrada:")
                    for i, m in enumerate(mensajes):
                        print(f"{i}: {m}")
                else:
                    print("No hay mensajes en la bandeja de entrada.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "4":
            correo = input("Ingrese el correo del usuario: ")
            nombre_carpeta = input("Ingrese el nombre de la nueva carpeta (raíz): ")
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                carpeta = Carpeta(nombre_carpeta)
                usuario.crear_carpeta(carpeta)
                print(f"Carpeta '{nombre_carpeta}' creada correctamente en la raíz.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "5":
            correo = input("Ingrese el correo del usuario: ")
            padre_nombre = input("Ingrese el nombre de la carpeta padre: ")
            sub_nombre = input("Ingrese el nombre de la nueva subcarpeta: ")
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                padre = servidor._buscar_carpeta_en_usuario(usuario, padre_nombre)
                if padre:
                    subcarpeta = Carpeta(sub_nombre)
                    padre.agregar_subcarpeta(subcarpeta)
                    print(f"Subcarpeta '{sub_nombre}' creada en '{padre_nombre}'.")
                else:
                    print("Carpeta padre no encontrada.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "6":
            correo = input("Ingrese el correo del usuario: ")
            nombre_carpeta = input("Ingrese el nombre de la carpeta: ")
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                carpeta = servidor._buscar_carpeta_en_usuario(usuario, nombre_carpeta)
                if carpeta:
                    mensajes = servidor.listar_mensajes(carpeta)
                    if mensajes:
                        print(f"\nMensajes en la carpeta {nombre_carpeta}:")
                        for i, m in enumerate(mensajes):
                            print(f"{i}: {m}")
                    else:
                        print(f"No hay mensajes en la carpeta {nombre_carpeta}.")
                else:
                    print("Carpeta no encontrada.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "7":
            correo = input("Ingrese el correo del usuario: ")
            origen_nombre = input("Nombre de la carpeta origen: ")
            destino_nombre = input("Nombre de la carpeta destino: ")
            try:
                indice = int(input("Índice del mensaje a mover (desde 0): "))
            except ValueError:
                print("Índice no válido.")
                continue
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                if servidor.mover_mensaje(usuario, origen_nombre, destino_nombre, indice):
                    print("Mensaje movido correctamente.")
                else:
                    print("Error: Carpeta o mensaje no encontrado.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "8":
            correo = input("Ingrese el correo del usuario: ")
            asunto = input("Ingrese el asunto a buscar: ")
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                resultados = servidor.buscar_mensajes_por_asunto(usuario, asunto)
                if resultados:
                    print("\nResultados de búsqueda por asunto:")
                    for m in resultados:
                        print(m)
                else:
                    print("No se encontraron mensajes.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "9":
            correo = input("Ingrese el correo del usuario: ")
            remitente = input("Ingrese el correo del remitente a buscar: ")
            usuario = next((u for u in servidor.usuarios if u.correo == correo), None)
            if usuario:
                resultados = servidor.buscar_mensajes_por_remitente(usuario, remitente)
                if resultados:
                    print("\nResultados de búsqueda por remitente:")
                    for m in resultados:
                        print(m)
                else:
                    print("No se encontraron mensajes.")
            else:
                print("Usuario no encontrado.")
        
        elif opcion == "10":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()