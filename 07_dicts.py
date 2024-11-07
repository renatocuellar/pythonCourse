# Diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))

my_other_dict = {"Nombre": "Renato", "Apellido": "Cuéllar", "Edad": 35, 1: "Python"}
print(my_other_dict)

my_dict = {
    "Nombre": "Renato", 
    "Apellido": "Cuéllar", 
    "Edad": 35, 
    "Lenguajes": {"Python", "JavaScript", "Java"},
    1:1.85
    }
print(my_dict)

print(my_dict["Nombre"])

my_dict["Address"] = "Calle 127"
print(my_dict)

del my_dict["Address"]
print(my_dict)

print("Renato" in my_dict)
print("Nombre" in my_dict)
print(my_dict["Apellido"])

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

# Se crea un diccionario nuevo sin valores
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)