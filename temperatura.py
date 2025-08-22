A=(int(input("Holaaa, bienvenido a la maravillosa calculadora todo-en-uno que permite convertir valores de una escala a otra. Por favor, selecciona la escala origen: \n 1. Celsius \n 2. Fahrenheit \n 3. Kelvin \n")))
B=(int(input("Ahora, selecciona la escala a la que deseas convertir: \n 1. Celsius \n 2. Fahrenheit \n 3. Kelvin \n")))
C=(float(input("Por favor, ingresa el valor que deseas convertir :))))))) \n")))
try:
    if A==1 and B==2:
     print("El resultado de la conversión de celsius a farenheit es " + str(((C * 1.8)+32)))
    elif A==1 and B==3:
     print("El resultado de la conversión de celsius a kelvin es " + str((C + 273.15)))
    elif A==2 and B==1:
        print("El resultado de la conversión de farenheit a celsius es " + str(((C - 32) / 1.8)))
    elif A==2 and B==3:
        print("El resultado de la conversión de farenheit a kelvin es " + str((((C - 32) / 1.8) + 273.15)))
    elif A==3 and B==1:
     print("El resultado de la conversión de kelvin a celsius es " + str((C - 273.15)))
    elif A==3 and B==2:
     print("El resultado de la conversión de kelvin a farenheit es " + str((((C - 273.15) * 1.8) + 32)))
except ValueError: 
    print("Algo hiciste mal crzn")