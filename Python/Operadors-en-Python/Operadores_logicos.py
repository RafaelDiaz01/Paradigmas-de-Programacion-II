#Kevin Rafael Díaz López

operador= input("Ingrese SI o NO: ")
operador=operador.lower()=="si"
print(f"¿Lo que ingresó es SI? {operador}")
print()

operador2= input("De nuevo ingrese SI o NO: ")
operador2=operador2.lower()=="no"
print(f"¿Lo que ingresó es NO? {operador2}")

print()
print(f"¿En los 2 casos el resultado fue verdadero? {operador and operador2}")

print()
print(f"¿En algun caso el resultado fue verdadero? {operador or operador2}")

print()
print(f"¿En la primer pregunta el resultado fue verdadero? {not operador}")