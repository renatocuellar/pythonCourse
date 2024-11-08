# Loops

# Bucle While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("Mi condición es mayor a 10")
print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 16:
        print("Mi condición es 16")
        break
    print(my_condition)