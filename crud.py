import os

# Archivo donde se almacenarán los datos
archivo = "datos.txt"

# Crear archivo si no existe
def inicializar_archivo():
    if not os.path.exists(archivo):
        with open(archivo, 'w') as f:
            pass

# Crear/Agregar un nuevo usuario
def crear_usuario(id_usuario, nombre, edad):
    with open(archivo, 'a') as f:
        f.write(f"{id_usuario},{nombre},{edad}\n")
    print(f"Usuario {nombre} agregado con éxito.")

# Leer usuarios del archivo
def leer_usuarios():
    with open(archivo, 'r') as f:
        usuarios = f.readlines()
    if not usuarios:
        print("No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            id_usuario, nombre, edad = usuario.strip().split(',')
            print(f"ID: {id_usuario}, Nombre: {nombre}, Edad: {edad}")

# Actualizar un usuario específico
def actualizar_usuario(id_usuario, nuevo_nombre, nueva_edad):
    usuarios_actualizados = []
    actualizado = False
    with open(archivo, 'r') as f:
        usuarios = f.readlines()
    for usuario in usuarios:
        datos = usuario.strip().split(',')
        if datos[0] == id_usuario:
            usuarios_actualizados.append(f"{id_usuario},{nuevo_nombre},{nueva_edad}\n")
            actualizado = True
        else:
            usuarios_actualizados.append(usuario)
    
    with open(archivo, 'w') as f:
        f.writelines(usuarios_actualizados)

    if actualizado:
        print(f"Usuario con ID {id_usuario} actualizado.")
    else:
        print(f"Usuario con ID {id_usuario} no encontrado.")

# Eliminar un usuario específico
def eliminar_usuario(id_usuario):
    usuarios_restantes = []
    eliminado = False
    with open(archivo, 'r') as f:
        usuarios = f.readlines()
    for usuario in usuarios:
        datos = usuario.strip().split(',')
        if datos[0] != id_usuario:
            usuarios_restantes.append(usuario)
        else:
            eliminado = True
    
    with open(archivo, 'w') as f:
        f.writelines(usuarios_restantes)
    
    if eliminado:
        print(f"Usuario con ID {id_usuario} eliminado.")
    else:
        print(f"Usuario con ID {id_usuario} no encontrado.")

# Menú para interactuar con el CRUD
def menu():
    inicializar_archivo()
    while True:
        print("\n--- CRUD de Usuarios con Archivos de Texto ---")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            id_usuario = input("ID del usuario: ")
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            crear_usuario(id_usuario, nombre, edad)
        
        elif opcion == '2':
            leer_usuarios()
        
        elif opcion == '3':
            id_usuario = input("ID del usuario a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_edad = input("Nueva edad: ")
            actualizar_usuario(id_usuario, nuevo_nombre, nueva_edad)
        
        elif opcion == '4':
            id_usuario = input("ID del usuario a eliminar: ")
            eliminar_usuario(id_usuario)
        
        elif opcion == '5':
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
