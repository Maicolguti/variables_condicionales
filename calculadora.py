A=input("Holaaa bienvenido a la calculadora re wow, ingresa la operación que quieres realizar \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n ")
match A:
    case "1":
      B=input("Ingresa el primer número a sumar ")
      C=input("Ingresa el segundo número a sumar ")
      print(f"El resultado de la suma es " + str(int(B)+int(C)))
    case "2":
      B=input("Ingresa el primer número a restar ")
      C=input("Ingresa el segundo número a restar ")
      print(f"El resultado de la resta es " + str(int(B)-int(C)))

    case "3":
      B=input("Ingresa el primer número a multiplicar ")
      C=input("Ingresa el segundo número a multiplicar ")
      print(f"El resultado de la multiplicación es " + str(int(B)*int(C)))

    case "4":
      B=input("Ingresa el primer número a dividir ")
      C=input("Ingresa el segundo número a dividir ")
      print(f"El resultado de la división es " + str(int(B)/int(C)))
    case _:
        print("No seleccionaste una opción de la lista :(")