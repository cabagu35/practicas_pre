#Ejercicio 1: Consulta

#Función 1:
def consulta_raw(archivo):
    texto = open(archivo, mode='r')
    contenido = texto.read()
    texto.close()
    return contenido

#Función 2:
def consulta_lines(archivo):
    texto = open(archivo, mode='r')
    for linea in texto:
        print(linea.strip())
    texto.close()
    return

#Función 3:
def consulta_lines_with(archivo):
    lista = []
    with open(archivo, mode='r') as texto:
        for linea in texto:
            lista.append(linea.strip())
    return lista



#Programa principal:
archivo = 'consulta.txt'
print(consulta_lines(archivo))
