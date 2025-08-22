A=float(input("Bienvenido seas, mi hermanito, a la calculadora de descuentos de la empresa; porque no sabes usar una calculadora normal. Te invito a digitar el valor del producto a descuentar \n"))
B=input("¿Es un cliente preferencial? Responde Y para sí y N para no ")
try:
  if A<10000:
    if B=="N":
      print("El producto no alcanza el suficiente precio como para aplicar un descuento")
    elif B=="Y":
        print("El precio del producto luego de aplicar el 5% de descuento por ser cliente preferencial es de " + str(A*0.95)) 
  elif A>=10000 and A<50000:
    if B=="N":
      print("El precio del producto luego de aplicar el 5% de descuento es de " + str(A*0.95)) 
    elif B=="Y": 
        print("El precio del producto luego de aplicar el 10% de descuento por ser cliente preferencial es de " + str(A*0.90)) 
  elif A >= 50000 and A <= 100000:
    if B=="N":
      print("El precio del producto luego de aplicar el 10% de descuento es de " + str(A*0.90))
    elif B=="Y":
      print("El precio del producto luego de aplicar el 15% de descuento por ser cliente profesional es de " + str(A*0.85))
  elif A > 100000:
    if B=="N":
      print("El precio del producto luego de aplicar el 15% de descuento es de " + str(A*0.85))
    elif B=="Y":
      print("El precio del producto luego de aplicar el 20% de descuento por ser cliente profesional es de " + str(A*0.80))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número para el valor del producto.")