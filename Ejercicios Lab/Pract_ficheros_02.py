#Ejercicio 2: El Invitado

#Función
def reg_invitados(archivo):
    with open(archivo, 'a') as invitados:
        nombre = input("¿Cómo se llama el nuevo invitado?: ")
        invitados.write(nombre+'\n')




#Programa principal:
archivo = 'invitados.txt'
reg_invitados(archivo)

