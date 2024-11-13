"""
Nivel 1
Descripción:

Crea un programa que muestre un menú en la consola con las siguientes opciones:

Agregar tarea
Mostrar tareas
Salir
El programa debe:

Mostrar el menú al usuario.
Solicitar al usuario que ingrese una opción (1, 2 o 3).
Mostrar un mensaje que indique qué opción ha seleccionado el usuario.
Repetir este proceso hasta que el usuario elija la opción 3 (Salir).
Pistas:

Usa un bucle while para mantener el programa ejecutándose hasta que el usuario decida salir.
Utiliza la función input() para capturar la elección del usuario.
Convierte la entrada del usuario a un número entero para facilitar las comparaciones.
Puedes usar condicionales if, elif, else para determinar qué mensaje mostrar según la opción elegida.
Objetivo:

Familiarizarte con la estructura básica del programa, manejando entradas del usuario, bucles y condicionales.


# Bucle para mostrar el menú de opciones
while True:
    # Mostrar el menú de opciones
    print("Menú de Tareas:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Salir")
    
    # Solicitar al usuario que elija una opción
    opcion = int(input("Elige una opción (1, 2, 3): "))
    
    # Verificar qué opción eligió el usuario
    if opcion == 1:
        print("Has elegido: Agregar tarea")
        # Aquí en el futuro agregaremos la lógica para agregar tareas
        
    elif opcion == 2:
        print("Has elegido: Mostrar tareas")
        # Aquí en el futuro agregaremos la lógica para mostrar las tareas
        
    elif opcion == 3:
        print("Has elegido: Salir")
        break  # Rompe el bucle para salir del programa
    
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 3.")

Nivel 2
Descripción:

Modifica el programa para que la opción Agregar tarea permita al usuario ingresar una tarea y almacenarla en una lista llamada tareas. Cada vez que el usuario elija la opción 1,
 se le debe pedir que ingrese el nombre de la tarea, y luego esa tarea se añade a la lista tareas.

Pistas:

Crea una lista vacía llamada tareas al inicio del programa.
Cuando el usuario elija la opción 1 (Agregar tarea), usa input() para capturar la descripción de la tarea y añade la tarea a la lista usando tareas.append(tarea).
Asegúrate de que el menú sigue apareciendo después de que el usuario agregue una tarea.
Objetivo:

Aprender a manipular listas en Python y entender cómo almacenar datos introducidos por el usuario en una estructura de datos.
"""
"""
Nivel 3
Ahora vamos a mejorar la funcionalidad de la opción Mostrar tareas.

Descripción:

Modifica el programa para que, cuando el usuario elija la opción "Mostrar tareas", se impriman todas las tareas en la lista tareas. Si la lista está vacía, 
muestra un mensaje que indique que no hay tareas para mostrar.

Pistas:

Usa una condición (if) para verificar si la lista tareas está vacía.
Si la lista tiene tareas, muestra cada tarea de manera ordenada.
Si la lista está vacía, imprime "No hay tareas para mostrar."
Objetivo:

Aprender a verificar si una lista está vacía y a mostrar su contenido de manera adecuada.

Cuando tengas esta parte lista, envíamela y avanzaremos al siguiente nivel. ¡Vamos bien!
"""
"""
Nivel 4
Ahora vamos a agregar una nueva funcionalidad: Eliminar tarea.

Descripción:

Añade una nueva opción al menú para Eliminar tarea. Cuando el usuario elija esta opción, muestra todas las tareas numeradas (1, 2, 3, ...) 
y permite al usuario ingresar el número de la tarea que desea eliminar. Luego, elimina esa tarea de la lista.

Pistas:

Usa enumerate() en el bucle for para mostrar las tareas con un índice.
Resta 1 del número ingresado por el usuario para obtener el índice correcto en la lista.
Asegúrate de manejar errores (por ejemplo, si el usuario elige un número que no existe en la lista).
Objetivo:

Practicar el uso de enumerate() y trabajar con índices en listas.

Nivel 5: Marcar Tarea como Completada
Vamos a añadir la funcionalidad para marcar una tarea como completada. 
En esta parte, actualizaremos la estructura de datos para almacenar el 
estado de cada tarea (completada o pendiente) y permitir al usuario cambiar este estado.


¡Excelente trabajo hasta ahora! Vamos al siguiente nivel.

Nivel 6: Filtrar y Mostrar Solo las Tareas Completadas o Pendientes
En este nivel, agregaremos una opción para que el usuario pueda ver solo las tareas completadas o solo las tareas pendientes.

Nivel 7: Editar Tarea
Este nivel te permitirá actualizar la descripción de una tarea. 
Añadiremos una nueva opción en el menú para editar una tarea, 
donde el usuario podrá elegir una tarea existente y cambiar su descripción.

¡Estás avanzando muy bien! Ahora vamos a añadir una funcionalidad que hace nuestro programa aún más robusto: la capacidad de guardar y cargar las tareas en un archivo. 
Esto permitirá que las tareas se mantengan guardadas, incluso si el programa se cierra, y que puedas cargarlas al iniciar el programa nuevamente.

Nivel 8: Guardar y Cargar Tareas en un Archivo
Vamos a implementar dos nuevas funciones en el programa:

Guardar tareas: Cuando el usuario elija salir, las tareas se guardarán en un archivo de texto (o JSON) automáticamente.
Cargar tareas al inicio: Cuando el programa inicia, cargará las tareas guardadas anteriormente desde el archivo.
Para este ejercicio, usaremos el formato JSON, que es fácil de leer y permite almacenar listas de diccionarios.

Paso 1: Importar el Módulo json
Al inicio del programa, importa el módulo json que nos permitirá guardar y cargar los datos en formato JSON.

¡Estás haciendo un gran trabajo! Ahora que el programa puede guardar y cargar tareas, vamos a agregar una última funcionalidad avanzada para hacer la aplicación aún más completa.

Nivel 9: Búsqueda de Tareas
En este nivel, implementaremos una opción que permita al usuario buscar tareas por palabra clave en la descripción. 
Esta funcionalidad será útil para que el usuario encuentre rápidamente una tarea específica en listas largas.
"""
"""
import json

# Función para guardar las tareas en un archivo JSON
def guardar_tareas(tareas):
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

# Función para cargar las tareas desde un archivo JSON
def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Lista para almacenar las tareas, cargada desde el archivo al inicio
tareas = cargar_tareas()

# Bucle para mostrar el menú de opciones
while True:
    # Mostrar el menú de opciones
    print("Menú de Tareas:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Filtrar tareas")
    print("6. Editar tarea")
    print("7. Guardar y salir")
    print("8. Buscar tarea")  # Nueva opción para buscar
    print("9. Salir")
    
    # Solicitar al usuario que elija una opción
    opcion = int(input("Elige una opción (1, 2, 3, 4, 5, 6, 7, 8, 9): "))
    
    # Verificar qué opción eligió el usuario
    if opcion == 1:
        print("Has elegido: Agregar tarea")
        tarea_desc = input("Ingresa la descripción de la tarea: ")
        tarea = {"descripcion": tarea_desc, "completada": False}
        tareas.append(tarea)
        print("Tarea agregada con éxito.")
        
    elif opcion == 2:
        print("Has elegido: Mostrar tareas")
        if not tareas:
            print("No hay tareas para mostrar.")
        else:
            for i, tarea in enumerate(tareas, 1):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i}. {tarea['descripcion']} - {estado}")
                
    elif opcion == 3:
        print("Has elegido: Eliminar tarea")
        if not tareas:
            print("No hay tareas para eliminar.")
        else:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea['descripcion']}")
            
            num_tarea = int(input("Ingrese el número de la tarea que desea eliminar: "))
            
            if 1 <= num_tarea <= len(tareas):
                del tareas[num_tarea - 1]
                print("Tarea eliminada con éxito.")
            else:
                print("Número de tarea no válido.")
                
    elif opcion == 4:
        print("Has elegido: Marcar tarea como completada")
        if not tareas:
            print("No hay tareas para marcar como completadas.")
        else:
            for i, tarea in enumerate(tareas, 1):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{i}. {tarea['descripcion']} - {estado}")
            
            num_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
            
            if 1 <= num_tarea <= len(tareas):
                tareas[num_tarea - 1]["completada"] = True
                print("Tarea marcada como completada.")
            else:
                print("Número de tarea no válido.")
                
    elif opcion == 5:
        print("Has elegido: Filtrar tareas")
        filtro = int(input("Elige una opción de filtro:\n1. Ver solo tareas completadas\n2. Ver solo tareas pendientes\n"))
        
        if filtro == 1:
            print("Tareas Completadas:")
            tareas_filtradas = [tarea for tarea in tareas if tarea["completada"]]
            if not tareas_filtradas:
                print("No hay tareas completadas.")
            else:
                for tarea in tareas_filtradas:
                    print("-", tarea["descripcion"])
                    
        elif filtro == 2:
            print("Tareas Pendientes:")
            tareas_filtradas = [tarea for tarea in tareas if not tarea["completada"]]
            if not tareas_filtradas:
                print("No hay tareas pendientes.")
            else:
                for tarea in tareas_filtradas:
                    print("-", tarea["descripcion"])
        else:
            print("Opción de filtro no válida.")
    
    elif opcion == 6:
        print("Has elegido: Editar tarea")
        if not tareas:
            print("No hay tareas para editar.")
        else:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea['descripcion']}")
            
            num_tarea = int(input("Ingrese el número de la tarea que desea editar: "))
            
            if 1 <= num_tarea <= len(tareas):
                nueva_descripcion = input("Ingresa la nueva descripción de la tarea: ")
                tareas[num_tarea - 1]["descripcion"] = nueva_descripcion
                print("Tarea editada con éxito.")
            else:
                print("Número de tarea no válido.")
                
    elif opcion == 7:
        print("Has elegido: Guardar y salir")
        guardar_tareas(tareas)  # Guardar las tareas antes de salir
        break  # Rompe el bucle para salir del programa

    elif opcion == 8:
        print("Has elegido: Buscar tarea")
        if not tareas:
            print("No hay tareas para buscar.")
        else:
            palabra_clave = input("Ingresa la palabra clave para buscar: ").lower()
            tareas_encontradas = [tarea for tarea in tareas if palabra_clave in tarea["descripcion"].lower()]
            
            if not tareas_encontradas:
                print("No se encontraron tareas con esa palabra clave.")
            else:
                print("Tareas encontradas:")
                for tarea in tareas_encontradas:
                    estado = "Completada" if tarea["completada"] else "Pendiente"
                    print(f"- {tarea['descripcion']} - {estado}")
                
    elif opcion == 9:
        print("Has elegido: Salir")
        break  # Rompe el bucle para salir del programa
    
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 9.")

"""
"""
¡Felicidades por llegar tan lejos! Vamos al último nivel, donde haremos una optimización general y mejoraremos la estructura del código. Este paso es importante porque te ayuda a organizar el código en funciones, haciendo que sea más modular y fácil de mantener. Esto es especialmente útil en una aplicación con múltiples funcionalidades, como la que has creado.

Nivel 10: Refactorización y Organización del Código en Funciones
Dividiremos el código en funciones individuales para cada operación, lo que mejorará la claridad y permitirá la reutilización.
"""

import json

# Función para guardar las tareas en un archivo JSON
def guardar_tareas(tareas):
    with open("tareas.json", "w") as archivo:
        json.dump(tareas, archivo)

# Función para cargar las tareas desde un archivo JSON
def cargar_tareas():
    try:
        with open("tareas.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

# Función para agregar una tarea
def agregar_tarea(tareas):
    tarea_desc = input("Ingresa la descripción de la tarea: ")
    tarea = {"descripcion": tarea_desc, "completada": False}
    tareas.append(tarea)
    print("Tarea agregada con éxito.")

# Función para mostrar todas las tareas
def mostrar_tareas(tareas):
    if not tareas:
        print("No hay tareas para mostrar.")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea["completada"] else "Pendiente"
            print(f"{i}. {tarea['descripcion']} - {estado}")

# Función para eliminar una tarea
def eliminar_tarea(tareas):
    if not tareas:
        print("No hay tareas para eliminar.")
    else:
        mostrar_tareas(tareas)
        num_tarea = int(input("Ingrese el número de la tarea que desea eliminar: "))
        if 1 <= num_tarea <= len(tareas):
            del tareas[num_tarea - 1]
            print("Tarea eliminada con éxito.")
        else:
            print("Número de tarea no válido.")

# Función para marcar una tarea como completada
def marcar_tarea_completada(tareas):
    if not tareas:
        print("No hay tareas para marcar como completadas.")
    else:
        mostrar_tareas(tareas)
        num_tarea = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
        if 1 <= num_tarea <= len(tareas):
            tareas[num_tarea - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea no válido.")

# Función para filtrar tareas
def filtrar_tareas(tareas):
    filtro = int(input("Elige una opción de filtro:\n1. Ver solo tareas completadas\n2. Ver solo tareas pendientes\n"))
    if filtro == 1:
        tareas_filtradas = [tarea for tarea in tareas if tarea["completada"]]
        if tareas_filtradas:
            for tarea in tareas_filtradas:
                print("-", tarea["descripcion"])
        else:
            print("No hay tareas completadas.")
    elif filtro == 2:
        tareas_filtradas = [tarea for tarea in tareas if not tarea["completada"]]
        if tareas_filtradas:
            for tarea in tareas_filtradas:
                print("-", tarea["descripcion"])
        else:
            print("No hay tareas pendientes.")
    else:
        print("Opción de filtro no válida.")

# Función para editar una tarea
def editar_tarea(tareas):
    if not tareas:
        print("No hay tareas para editar.")
    else:
        mostrar_tareas(tareas)
        num_tarea = int(input("Ingrese el número de la tarea que desea editar: "))
        if 1 <= num_tarea <= len(tareas):
            nueva_descripcion = input("Ingresa la nueva descripción de la tarea: ")
            tareas[num_tarea - 1]["descripcion"] = nueva_descripcion
            print("Tarea editada con éxito.")
        else:
            print("Número de tarea no válido.")

# Función para buscar una tarea por palabra clave
def buscar_tarea(tareas):
    if not tareas:
        print("No hay tareas para buscar.")
    else:
        palabra_clave = input("Ingresa la palabra clave para buscar: ").lower()
        tareas_encontradas = [tarea for tarea in tareas if palabra_clave in tarea["descripcion"].lower()]
        if tareas_encontradas:
            for tarea in tareas_encontradas:
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"- {tarea['descripcion']} - {estado}")
        else:
            print("No se encontraron tareas con esa palabra clave.")

# Lista para almacenar las tareas, cargada desde el archivo al inicio
tareas = cargar_tareas()

# Bucle para mostrar el menú de opciones
while True:
    # Mostrar el menú de opciones
    print("\nMenú de Tareas:")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Marcar tarea como completada")
    print("5. Filtrar tareas")
    print("6. Editar tarea")
    print("7. Guardar y salir")
    print("8. Buscar tarea")
    print("9. Salir")
    
    # Solicitar al usuario que elija una opción
    opcion = int(input("Elige una opción (1-9): "))
    
    # Llamar a la función correspondiente según la opción elegida
    if opcion == 1:
        agregar_tarea(tareas)
    elif opcion == 2:
        mostrar_tareas(tareas)
    elif opcion == 3:
        eliminar_tarea(tareas)
    elif opcion == 4:
        marcar_tarea_completada(tareas)
    elif opcion == 5:
        filtrar_tareas(tareas)
    elif opcion == 6:
        editar_tarea(tareas)
    elif opcion == 7:
        guardar_tareas(tareas)
        print("Tareas guardadas. Saliendo del programa...")
        break
    elif opcion == 8:
        buscar_tarea(tareas)
    elif opcion == 9:
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, elige una opción entre 1 y 9.")


