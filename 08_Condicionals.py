# Condicionales
# Si se cumple una condicion, se ejecuta

my_condition = False

if my_condition: #Es lo mismo que if my_condition == True
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es maypor a 10 y menos que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual a 10 o mayor o igual a 20")


print("la ejecución continúa")  