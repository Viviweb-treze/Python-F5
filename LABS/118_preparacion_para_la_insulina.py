
# limpieza de codigo manual
preproinsulin = 'malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn'

caracteres = len(preproinsulin)

print("Total caracteres --> ", caracteres)  # compruebo longitud

# creo las subcadenas y las meto en una funcion:


def insulina():
    isinsulin = (preproinsulin[:23])
    binsulin = (preproinsulin[24:53])
    cinsulin = (preproinsulin[54:88])
    ainsulin = (preproinsulin[89:109])
    print("Isinsulin --> ", isinsulin)
    print("Binsulin --> ", binsulin)
    print("Cinsulin --> ", cinsulin)
    print("Ainsulin --> ", ainsulin)


insulina()
