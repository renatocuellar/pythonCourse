"""
Nivel 1
Descripción:
Crea una lista con los números del 1 al 10 e imprime el contenido de la lista.

Pista:
Usa la sintaxis de listas de Python para declarar los números directamente en la lista. Luego, utiliza la función print() para mostrar el contenido.

Cuando tengas la respuesta de este nivel, envíamela, y te daré el siguiente nivel. ¡Buena suerte!
"""
# Crear una lista de números del 1 al 10
sequence_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sequence_of_numbers)

"""
Nivel 2
Descripción:
Ahora que tienes la lista de números del 1 al 10, 
calcula la suma de todos los elementos en la lista 
y almacénala en una nueva variable llamada suma_total. 
Luego, imprime suma_total.

Pista:
Usa la función sum() para calcular la suma de todos los elementos en numbers_list.

Cuando tengas la respuesta de este nivel, envíamela, y pasaremos al siguiente nivel.
"""
# Suma total de los elementos de la lista
suma_total = sum(sequence_of_numbers)
print(suma_total)

"""
Nivel 3
Descripción:
Ahora que tienes la suma de todos los elementos, calcula el promedio de los números en sequence_of_numbers. 
Almacena el resultado en una variable llamada promedio e imprímelo.

Pista:
Recuerda que el promedio se obtiene dividiendo la suma total de los elementos por la cantidad de elementos. 
Usa la función len() para obtener el número de elementos en la lista.

Cuando tengas la respuesta de este nivel, envíamela, y avanzaremos al siguiente. ¡Sigue así!
"""
# Calculo del promedio de los números en sequence_of_numbers
promedio = suma_total/len(sequence_of_numbers)
print(promedio)

"""
Nivel 4
Descripción:
Ahora, queremos crear una nueva lista llamada numeros_pares que contenga solo los números pares de sequence_of_numbers.

Pista:
Para determinar si un número es par, puedes usar el operador de módulo (%). Un número es par si el residuo de su división por 2 es 0. 
Utiliza solo los conceptos que has aprendido hasta ahora.

Cuando tengas la respuesta de este nivel, envíamela para que avancemos al último nivel. ¡Sigue así,
"""
# Crear una nueva lista con solo los números pares
numeros_pares = [sequence_of_numbers[1], sequence_of_numbers[3], sequence_of_numbers[5], sequence_of_numbers[7], sequence_of_numbers[9]]
print(numeros_pares)

"""
Nivel 5
Descripción:
En este nivel final, queremos calcular la suma de los números pares en la lista numeros_pares que 
creaste en el nivel anterior y almacenar el resultado en una variable llamada suma_pares. Luego, imprime suma_pares.

Pista:
Ya tienes una lista que contiene solo los números pares. Usa la función sum() 
para obtener la suma de los elementos de numeros_pares y guárdala en suma_pares.

Cuando tengas la respuesta, compártela conmigo. ¡Este es el último paso!
"""
# Suma de todos los números pares
suma_pares = sum(numeros_pares)
print(suma_pares)