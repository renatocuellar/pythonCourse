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

#Inferencia de datos (anteponiendo la f)

print(f"Mi nombre es {name} {surname} y mi edad es {age}")


# Desempaquetado de caracteres

language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

#división

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

#Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count(language))
print(language.isnumeric)
print(language.lower())