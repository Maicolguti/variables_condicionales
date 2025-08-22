A=int(input("Hola, bienvenido a la calculadora de edad para votar. Para empezar, digita tu edad \n"))
B=int(input("Ahora elige uno de los siguientes paises: \n 1. Austria \n 2. Colombia \n 3. Emiratos Arabes Unidos \n 4. Kuwait \n 5. Corea del sur \n"))
try:
    if B==1:
        if A>=16:
            print("Enhorabuena chaval!! puedes votar.")
        else:
            print("Nonas mi león, no puedes votar aún, espera " + str(16-A) + " años.")
    elif B==2:
        if A>=18:
            print("Enhorabuena chaval!! puedes votar.")
        else:
            print("Nonas mi león, no puedes votar aún, espera " + str(18-A) + " años.")
    elif B==3:
        if A>=25:
            print("Enhorabuena chaval!! puedes votar.")
        else:
            print("Nonas mi león, no puedes votar aún, espera " + str(25-A) + " años.")
    elif B==4:
        if A>=21:
            print("Enhorabuena chaval!! puedes votar.")
        else:
            print("Nonas mi león, no puedes votar aún, espera " + str(21-A) + " años.")
    elif B==5:
        if A>=19:
            print("Enhorabuena chaval!! puedes votar.")
        else:
            print("Nonas mi león, no puedes votar aún, espera " + str(19-A) + " años.")
except ValueError:
    print("Entrada inválida, por favor asegúrate de ingresar un número para la edad y un número de 1 a 5 según el respectivo país")