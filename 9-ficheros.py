# Leo un fichero CSV con código y nombre de paises
# https://docs.python.org/3/library/functions.html#open

fichero = open('archivo.txt', 'w')
fichero.write('hola mundo')
fichero.close()

fichero = open('archivo.txt', 'r')
print(fichero.read())
fichero.close()
