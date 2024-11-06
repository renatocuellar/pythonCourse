# Strings

My_string = "Mi primer string"
My_other_string = "Mi otro string"

print(len(My_string))
print(len(My_other_string))

print(My_string + " " + My_other_string)

# formateo

name, surname, age = "Renato", "Cuéllar", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d"%(name, surname, age))