"""
Área de un Triángulo
Crea un programa que solicite al usuario la base y la altura de un triángulo y calcule su área usando la fórmula:
Area = (Base x Altura)/2
Muestra el área resultante.

"""

base = int(input("Cuál es la base del triangulo "))
altura = int(input("Cuál es la altura del triangulo "))
area = (base*altura)/2

print("El área del triangulo es ", area)