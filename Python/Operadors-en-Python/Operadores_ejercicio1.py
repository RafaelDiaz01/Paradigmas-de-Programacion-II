#Kevin Rafael Díaz López

print("** \tBONIFICACIÓN DE BUEN FIN **")
cantidad_gastada = float(input("Cantidad gastada: "))
mayor = cantidad_gastada > 5000

meses = input("¿La compra fue a meses? ")
meses = meses.lower() == "si"


print(f"¿Aplica bonificación de Buen Fin? {mayor and meses}")