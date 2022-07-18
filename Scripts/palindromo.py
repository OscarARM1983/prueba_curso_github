from audioop import reverse


palabra = input("Ingrese una palabra: ")
lista_palabra = []

longitud = len(palabra)

for i in range(longitud):
    lista_palabra.append(palabra[i])

palabra_reves = []
verificacion = 1

for i in range(longitud-1, -1, -1):
    palabra_reves.append(lista_palabra[i])

#print(lista_palabra)
#print(palabra_reves)

for j in range(longitud):
    #print(lista_palabra[j])
    #print(palabra_reves[j])
    if lista_palabra[j] != palabra_reves[j]:
        verificacion = 0
        break

if verificacion == 0:   
    print(f"La palabra {palabra} no es un palíndromo")
else:
    print(f"La palabra {palabra} es un palíndromo")