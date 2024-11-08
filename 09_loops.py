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

# Bucle FOR

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list: #Listas
    print(element)

my_tuple = (35, 1.85, "Renato", "Cuéllar")

for element in my_tuple: #Tuplas
    print(element)

my_other_set = {"Renato", "Cuéllar", 35}

for element in my_other_set: #Sets
    print(element)


my_other_dict = {"Nombre": "Renato", "Apellido": "Cuéllar", "Edad": 35, 1: "Python"}

for element in my_other_dict: #Diccionarios
    print(element)

for element in my_other_dict.values():
    print(element)
    if element == 36:
        break
else:
    print("El bucle for ha finalizado")