'''
Ejercicio 1 - Trabajo con la instruccion if
'''

usuarioRespuesta = input(
    "¿Necesita enviar un paquete? (Ingrese si o no) -->  ")

if usuarioRespuesta == "si":
    print("¡Podemos ayudarlo a enviar ese paquete!")
else:
    # Ejercicio 2 - Trabajo con la instruccion else
    print("Por favor, vuelva cuando necesite enviar un paquete. Gracias.")


'''
Ejercicio 3 - Trabajo con la instrucción elif
'''

usuarioReply = input(
    "¿Le gustaría comprar sellos, comprar un sobre o hacer una copia? (Ingrese sellos, sobre o copia)")
if usuarioReply == "sellos":
    print("Tenemos muchos diseños de sellos para elegir.")
elif usuarioReply == "sobre":
    print("Tenemos muchos tamaños de sobres para elegir.")
elif usuarioReply == "copia":
    copias = input("¿Cuántas copias desea? (Ingrese un número) ")
    print("Aquí tiene sus {} copias".format(copias))
else:
    print("Gracias, por favor venga de nuevo.")
