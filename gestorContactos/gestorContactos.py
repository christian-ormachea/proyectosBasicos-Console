import os

contactos = []
nombre_archivo = "contactos.txt"
archivo_nuevo = False

def mostrarMenu():
    print("Que tareas desea realizar?")
    print("1. Cargar un archivo")
    print("2. Agregar un contacto.")
    print("3. Ver todos los contactos.")
    print("4. Buscar un contacto.")
    print("5. Eliminar un contacto.")
    print("6. Guardar contactos en un archivo.")
    print("7. Salir")

def cargarArchivo():
    global archivo_nuevo
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            for linea in archivo:
                nombre, telefono, email = linea.strip().split("|")
                contactos.append({"nombre": nombre, "telefono": telefono, "email": email})
    else:
        print("El archivo no se encontro, se creara uno nuevo!")
        archivo_nuevo = True

def agregarContacto():
    print("\n--- Agregar Contacto ---")
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print("Error!, el contacto ya existe!")
            return
    
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})

def listarContactos():
    print("\n--- Lista de Contactos---")
    i = 1

    if not contactos:
        print("No hay contactos registrados.")
    else:
        for contacto in contactos:
            print(f"{i}. Nombre: {contacto['nombre']}, Telefono: {contacto['telefono']}, Email: {contacto['email']}")
            i += 1

def buscarContacto(nombre):
    contactoEncontrado = None
    for contacto in contactos:
        if contacto["nombre"] == nombre:
            contactoEncontrado = contacto
            break
    
    if contactoEncontrado:
        print(f"Resultados de la busqueda: Nombre: {contactoEncontrado['nombre']}, Telefono: {contactoEncontrado['telefono']}, Email: {contactoEncontrado['email']}")
    else:
        print("No se encontro ningun contacto")
        return
    
def eliminarContacto(nombreAEliminar):
    for contacto in contactos:
        if contacto["nombre"].lower() == nombreAEliminar.lower():
            contactos.remove(contacto)
            print("¡Contacto eliminado con éxito!")
            return
    print("No se encontró el contacto.")

def guardarDatosEnArchivo():
    with open(nombre_archivo, 'w') as archivo:
        for contacto in contactos:
            archivo.write(f"{contacto['nombre']}|{contacto['telefono']}|{contacto['email']}\n")

def main():
    print("Bienvenido al gestor de contactos de Ormachea Christian")
    opcion = 0
    while opcion != 7:
        mostrarMenu()

        try: 
            opcion = int(input("Elija que opcion desea realizar: (1 al 7)"))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue

        if opcion not in [1, 2, 3, 4, 5, 6, 7]:
            print("Elija una opcion correcta")
            continue

        if opcion == 1:
            cargarArchivo()
        elif opcion == 2:
            agregarContacto()
        elif opcion == 3:
            listarContactos()
        elif opcion == 4:
            nombre = input("Ingrese el nombre que desea buscar: ")
            buscarContacto(nombre)
        elif opcion == 5:
            nombreAEliminar = input("Ingrese el nombre que desea eliminar: ")
            eliminarContacto(nombreAEliminar)
        elif opcion == 6:
            guardarDatosEnArchivo()
        elif opcion == 7:
            print("Saliendo del gestor de contactos...")

if __name__ == "__main__":
    main()