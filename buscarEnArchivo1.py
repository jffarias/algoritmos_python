
#https://es.stackoverflow.com/questions/38288/duda-con-raw-input
#http://pharalax.com/blog/python-buscador-de-palabras-en-un-archivo/

print("*** buscador de palabras dentro de un archivo ***")
print("*************************************************")
print ("")
palabra = input("palabra a buscar ?? ")
archivo = input("Archivo donde Buscar >> ")

repetidas = 0
f = open(archivo)
lines = f.readlines()
for line in lines:
    palabras = line.split(' ')
    for p in palabras:
        if p==palabra:
            repetidas = repetidas+1

print("la palabra \"{0}\" se repite {1} veces en el Archivo {2}".format(palabra,repetidas,archivo))
