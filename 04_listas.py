# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.85, "Renato", "Cuellar"]

print(my_other_list)

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

my_other_list.append("Matealva")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)