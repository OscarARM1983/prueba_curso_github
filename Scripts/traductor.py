traductor = {}

palabras = input("Ingrese las palabras que desea traducir con el formato 'Español:Inglés,': ")

lista_palabras = palabras.split(", ")
longitud = len(lista_palabras)

#print(lista_palabras[0])

for x in lista_palabras:
    llave, valor = x.split(":")
    traductor[llave] = valor
    
#print(traductor)

frase = input("Introduzca una frase en español para traducir: ")

lista_frase = frase.split(" ")
#print(lista_frase[0])
long_frase = len(lista_frase)

for y in lista_frase:
    if y in traductor:
        print(traductor[y], end=" ")
    else:
        print(y, end=" ")


