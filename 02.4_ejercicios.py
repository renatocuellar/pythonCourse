"""
Promedio de Cinco Números
Solicita cinco números al usuario y calcula su promedio. Usa operadores aritméticos para sumar los números y dividir el total entre cinco. Muestra el promedio.
"""

num1 = int(input("Dame el primer número? "))
num2 = int(input("Dame el segundo número? "))
num3 = int(input("Dame el tercer número? "))
num4 = int(input("Dame el cuarto número? "))
num5 = int(input("Dame el quinto número? "))

promedio = (num1+num2+num3+num4+num5)/5

print("El promedio de tus números es ", promedio)