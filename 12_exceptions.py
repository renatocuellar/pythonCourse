# Exceptions handling

#Basicamente siempre van a haber bugs. 
# Lo ideal que no se rompa la aplicación 
# si tenemos un error

number_one = 5
number_two = 1

#number_two = "1"

# Try Except

try:
    print(number_one + number_two)
except:
    print("Se ha producido un error")

    # Try Except else finally

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente")
finally:
    print("La ejecución continúa")

number_three = 45
number_four = "2"

try:
    print(number_three + number_four)
    print("No se ha producido un error")
except TypeError:
    print("Se ha producido un error")

#Capturar la información de la excepción

try:
    print(number_three + number_four)
    print("No se ha producido un error")
except ValueError as error:
    print(error)
except Exception as error:
    print(error)