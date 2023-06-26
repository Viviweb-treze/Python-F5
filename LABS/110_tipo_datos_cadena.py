"""
Ejercicio 1: Presentar el tipo de dato de cadena
"""

myString = "This is a string."
print(myString)

# string (varias formas de lo mismo)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))
print(f"{myString} is of the data type {(type(myString))}")
print("{} is of the data type {}".format(myString, type(myString)))

"""
Ejercicio 2: Trabajar con concatenación de cadenas
"""
primeraCadena = "lava"
segundaCadena = "dora"
finalCadena = primeraCadena + segundaCadena
print(finalCadena)

"""
Ejercicio 3: Trabajar con cadenas de entrada
"""

name = input("¿Cual es tu nombre?")
print(name)

"""
Ejercicio 4: Dar formato a las cadenas de salida
"""

color = input("¿Cual es tu color favorito?")
animal = input("¿Cual es tu animal favorito?")
# OJO, hay que ejecutar los tres inputs para que pueda recoger los datos en la siguiente linea.
print("Soy {}, me gusta el color {} y el {}".format(name, color, animal))
