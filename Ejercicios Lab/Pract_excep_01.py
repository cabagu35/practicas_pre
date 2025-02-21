#Practica excepciones 1
#No hay control de excepciones
# se acba con un ctrl+C


print('Practica excepciones: inicio')
while True:
    num = float(input('Entre Numerador: '))
    denom = float(input('Entre denominador:'))
    try:
        divisio= num/denom
        print('Division = %6.2f' % divisio)
        print('Adiós')
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")
