# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Renato", "Cuéllar", 35}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Matealva") #Un set no es una estructura ordenada
print(my_other_set) #Un set no admite repetidos


print("Cuéllar" in my_other_set)
print("Cuellar" in my_other_set)

my_other_set.remove("Matealva")
print(my_other_set)

#my_other_set.clear() Borra automaticamente todo el set
#print(len(my_other_set))

my_set = {"Python", "Javascript", "Swift"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

