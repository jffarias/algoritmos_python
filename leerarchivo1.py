#https://www.youtube.com/watch?v=Z__uTkV4888
#https://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python
import time

def leerArch():
    # Abre archivo en modo lectura
    archivo = open('datos1.txt','r')
    # Lee todas la líneas y asigna a lista
    lista = archivo.readlines()
    # Inicializa un contador
    numlin = 0
    # Recorre todas los elementos de la lista
    for linea in lista:
        # incrementa en 1 el contador
        numlin += 1
        # muestra contador y elemento (línea)
        if(numlin <= 5):
            print(numlin, linea)
    archivo.close()  # cierra archivo

while(True):
    time.sleep(5)
    print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
    leerArch()
