'''
Ejercicio 1 - Presentar el tipo de dato de lista
Definición de una lista
'''

miListaFrutas = ["Manzana", "Platano", "Tomate"]
print(miListaFrutas)
print(type(miListaFrutas))

'''
Acceso a una lista por posicion
'''

print(miListaFrutas[0])
print(miListaFrutas[1])
print(miListaFrutas[2])

'''
Modificación de valores de una lista
'''

miListaFrutas[2] = "Naranja"
print(miListaFrutas)

'''
Ejercicio 2 - Presentar el tipo de dato de tupla
'''
miTuplaFrutas = ("Manzana", "Platano", "Piña")
print(miTuplaFrutas[0])
print(miTuplaFrutas[1])
print(miTuplaFrutas[2])
print(miTuplaFrutas)

'''
Ejercicio 3 - Presentar el tipo de dato de diccionario
Definición de un diccionario
'''

miDiccionarioFrutas = {
    "Jose": "Manzana",
    "Juan": "Platano",
    "Pedro": "Piña"
}
print(miDiccionarioFrutas)
print(type(miDiccionarioFrutas))

'''
Acceso al diccionario por nombre
'''

print(miDiccionarioFrutas["Jose"])
print(miDiccionarioFrutas["Juan"])
print(miDiccionarioFrutas["Pedro"])
