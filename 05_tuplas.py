# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.85, "Renato", "Cuéllar")
my_other_tuple = (16, 25, 85, 32, 35)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Matealva"))
print(my_tuple.count("Cuéllar"))
print(my_tuple.index("Renato"))

# my_tuple[1] = 1.84 Las tuplas son inmutables
# print(my_tuple) Las listas si se pueden cambiar

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

del my_tuple #con esto se pueden eliminar las tuplas, y ya no existirían.

