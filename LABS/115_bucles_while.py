'''
Ejercicio 1 - Trabajo con un bucle while
'''

import random
print("¡Bienvenido a Adivina el Número!")
print("Las reglas son simples. Pensaré en un número y tú intentarás adivinarlo")


numero = random.randint(1, 10)

esCorrecta = False

while esCorrecta != True:
    adivina = input("Adivina un número entre 1 y 10: ")
    if int(adivina) == numero:
        print("Has dicho {}. Es correcto, eres el ganador".format(adivina))
        esCorrecta = True
    else:
        print("Has dicho {}. Lo siento, no es eso. Inténtalo de nuevo".format(adivina))
