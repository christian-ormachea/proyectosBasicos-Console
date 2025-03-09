import os

tareas = []
archivo_tareas = "tareas.txt"

def cargar_tareas():
    if os.path.exists(archivo_tareas):
        try:
            with open(archivo_tareas, 'r') as archivo:
                for linea in archivo:
                    nombreTarea, descripcion, completada = linea.strip().split("|")
                    tareas.append({"nombreTarea": nombreTarea, "descripcion": descripcion, "completada": completada == "True"})
        except Exception as e:
            print(f"Error al cargar las tareas: {e}")

def guardar_tareas():
    with open(archivo_tareas, 'w') as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['nombreTarea']}|{tarea['descripcion']}|{tarea['completada']}\n")

def agregar_tarea():
    print("\n ---- Agregar Tarea ----")
    print("Como se llama la tarea: \n")
    nombreTarea = input()
    print("Como describe la tarea: \n")
    descripcion = input()
    tareas.append({"nombreTarea": nombreTarea,"descripcion": descripcion,"completada": False})
    print("Tarea agregada con exito! ")

def ver_tareas():
    print("\n ---- Ver Tareas ----")
    i = 0
    if not tareas:
        print("No hay tareas para mostrar!")
    else:
        for tarea in tareas:
            print(f"{i}. Nombre de la tarea: {tarea['nombreTarea']} Descripcion de la tarea: {tarea['descripcion']} Completa?: {tarea['completada']}")
            i+=1

def marcar_tarea():
    print("\n ---- Marcar tarea ----")
    print("Como se llama la tarea que quiere marcar como completada?: \n")
    nombreTareaACompletar = input()
    tareaEncontrada = False
    if not tareas:
        print("No hay tareas para buscar!")
        return
    for tarea in tareas:
        if nombreTareaACompletar.lower() == tarea['nombreTarea'].lower():
            tarea['completada'] = True
            tareaEncontrada = True
            print(f"La tarea: {tarea['nombreTarea']} se ha marcado como completada!")
            break
    if not tareaEncontrada:
        print("No se encontro la tarea")

def eliminar_tarea():
    print("\n ---- Eliminar tarea ----")
    ver_tareas()
    try:
        numeroTareaAEliminar = int(input("Cual es el numero de la tarea que quiere eliminar?: ")) - 1
        if 0 <= numeroTareaAEliminar < len(tareas):
            tarea_eliminada = tareas.pop(numeroTareaAEliminar)
            print(f"La tarea: {tarea_eliminada['nombreTarea']} ha sido eliminada!")
        else:
            print("Numero de tarea no valido")
    except ValueError:
        print("Porfavor, ingrese un numero valido!")
    

def mostrar_menu():
    print("\n Bienvenido al gestor de tareas(To-DoList) de Christian")
    print("Seleccione la accion que desee realizar: ")
    print("1. Agregar Tarea")
    print("2. Ver Tareas")
    print("3. Marcar Tarea como Completada")
    print("4. Eliminar Tarea")
    print("5. Salir")


def main():
    opcion = 0
    cargar_tareas()
    while opcion != 5:
        mostrar_menu()
        opcion = input("Seleccione la accion: (1 al 5)")

        if opcion not in ["1", "2", "3", "4" ,"5"]:
            print("Elija una opcion correcta")
            continue
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            marcar_tarea()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            guardar_tareas()
            print("Saliendo del gestor de tareas...")
            break
        
if __name__ == "__main__":
    main()

