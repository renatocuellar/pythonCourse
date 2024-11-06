"""
Conversión de Minutos a Horas y Minutos
Escribe un programa que pida al usuario una cantidad de minutos y luego convierta esa cantidad en horas y minutos. 
Por ejemplo, si el usuario ingresa 150, el programa debe mostrar "2 horas y 30 minutos". 
Usa operadores para obtener la división y el residuo.
"""
# Solicitar al usuario una cantidad de minutos
minutos_totales = int(input("Ingresa la cantidad de minutos: "))

# Calcular las horas usando división entera
horas = minutos_totales // 60

# Calcular los minutos restantes usando el operador módulo
minutos_restantes = minutos_totales % 60

# Mostrar el resultado
print(f"{horas} horas y {minutos_restantes} minutos")580