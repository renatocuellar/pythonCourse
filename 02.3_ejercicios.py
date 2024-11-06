"""
Número Elevado al Cuadrado y al Cubo
Pide al usuario que ingrese un número. Calcula el cuadrado y el cubo de ese número y muestra ambos resultados. Usa el operador ** para elevar el número.
"""

numero = int(input("¿Cuál es el número que quieres elevar al cuadrado y al cubo? "))
cuadrado = numero ** 2
cubo = numero ** 3

print("El número elevado al cuadrado es ", cuadrado, " Y el número elevado al cubo es ", cubo)