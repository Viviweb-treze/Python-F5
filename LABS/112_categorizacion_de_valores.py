'''
Ejercicio 1 - Crear una lista de varios tipos 
'''

miListaMixta = [45, 290578, 1.02, True, "Mi perro está en la cama", "45"]
for contenido in miListaMixta:
    print("{} es de tipo {}".format(contenido, type(contenido)))
print("------------")
for contenido in miListaMixta:
    # lo mismo que arriba con otro tipo de string
    print(f"{contenido} es de tipo {type(contenido)}")
print("------------")
