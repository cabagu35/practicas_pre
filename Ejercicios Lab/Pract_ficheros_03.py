#Ejercicio 3: Libro Visitas

#Función:
def libro_visitas(archivo):
    with open(archivo, 'a') as libro:
        while True:
            nombre = input("¿Cómo se llama el nuevo invitado?: ")
            if nombre == "":
                return False
            libro.write(nombre + '\n')

