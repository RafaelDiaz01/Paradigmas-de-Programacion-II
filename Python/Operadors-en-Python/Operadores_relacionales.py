#Kevin Rafael Díaz López - 18/10/2024

numdecimal1 = float(input("Ingrese un número decimal: "))
numdecimal2 = float(input("Ingrese otro número decimal: "))
print()

print(f"¿El número {numdecimal1:.2f} es mayor que {numdecimal2:.2f}?")
mayor=numdecimal1>numdecimal2
print(mayor)

print(f"¿El número {numdecimal1:.2f} es mayor o igual que {numdecimal2:.2f}?")
mayorig=numdecimal1>=numdecimal2
print(mayorig)

print(f"¿El número {numdecimal1:.2f} es menor que {numdecimal2:.2f}?")
menor=numdecimal1<numdecimal2
print(menor)

print(f"¿El número {numdecimal1:.2f} es menor igual que {numdecimal2:.2f}?")
menorig=numdecimal1<=numdecimal2
print(menorig)

print(f"¿El número {numdecimal1:.2f} es igual que {numdecimal2:.2f}?")
igual=numdecimal1==numdecimal2
print(igual)

print(f"¿El número {numdecimal1:.2f} es diferente que {numdecimal2:.2f}?")
dif=numdecimal1!=numdecimal2
print(dif)



