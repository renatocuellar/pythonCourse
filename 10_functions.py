# Functions

def my_funtion ():
    print("Esto es una Función")

my_funtion ()

def sum_two_values (first_numer, second_number):
    print(first_numer ** second_number)

sum_two_values(5, 7)


def sum_two_values_return (firts_value, second_value):
    return firts_value + second_value

my_result = sum_two_values_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Renato", "Cuéllar")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Renato", "Cuéllar")
print_name_with_default("Renato", "Cuéllar", "Matealva")
