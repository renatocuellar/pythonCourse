# Classes

class MyPerson:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
person = MyPerson("Renato ", "Cuéllar")
print(f"{person.name}{person.surname}")
#Podemos crear diferentes tipos de clases
class Person:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"

    def walk(self):
        print(f"{self.full_name} está Caminando")

my_person = Person("Renato", "Valencia")
print(my_person.full_name)
my_person.walk()