#Kevin Rafael Díaz López - 14/10/2024
#Programa que define el presupuesto diario

presupuesto = 180

#Datos para el lunes
dia_lunes = "lunes" #Cadena de texto
pasaje_lunes = 20 #Número entero
comida_lunes = 135.5 #Número decimal
otros_gastos_lunes = 34.5 #Número decimal
total_gastos_lunes = pasaje_lunes + comida_lunes + otros_gastos_lunes
mayor_presupuesto_lunes = total_gastos_lunes > presupuesto

#Mostrar los gastos del lunes
print("*** Gastos diarios ***")
print(f"Día: {dia_lunes}")
print(f"Pasaje: {pasaje_lunes}")
print(f"Comida: {comida_lunes}")
print(f"Otros gastos: {otros_gastos_lunes}")
print(f"¿Fue mayor a mi presupuesto?: {mayor_presupuesto_lunes}")
print()  #Salto de línea

#Datos para el martes
dia_martes = "martes" #Cadena de texto
pasaje_martes = 12 #Número entero
comida_martes = 45.5 #Número decimal
otros_gastos_martes = 4.5 #Número decimal
total_gastos_martes = pasaje_martes + comida_martes + otros_gastos_martes
mayor_presupuesto_martes = total_gastos_martes > presupuesto

#Mostrar los gastos del martes
print("*** Gastos diarios ***")
print(f"Día: {dia_martes}")
print(f"Pasaje: {pasaje_martes}")
print(f"Comida: {comida_martes}")
print(f"Otros gastos: {otros_gastos_martes}")
print(f"¿Fue mayor a mi presupuesto?: {mayor_presupuesto_martes}")
