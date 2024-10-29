# Kevin Rafael Díaz López
# Ejercicio que simula un programa de Banco Azteca

print("\n\tBienvenido a tu cuenta de Banco Azteca")
i = 1
saldo = 0

while i != 0:
    print("[1] CONSULTAR SALDO")
    print("[2] INGRESAR DINERO")
    print("[3] RETIRAR DINERO")
    print("[0] SALIR")

    i = float(input("¿Que desea realizar? "))

    if i == 0 :
        print("S A L I S T E ")
        break
    elif i == 1 :
        print(f"\nSU SALDO ES DE ${saldo}\n")
    elif i == 2 :
        print("\nINGRESANDO DINERO")
        ingresar = int(input("CANTIDAD A INGRESAR: $"))
        if ingresar < 0 :
            print("INGRESA UNA CANTIDAD CORRECTA\n")
        else:
            saldo = ingresar
    elif i == 3 :
        print("\nRETIRANDO DINERO")
        retirar = int(input("CANTIDAD A RETIRAR: $"))

        if retirar < 0 :
            print("INGRESA UNA CANTIDAD CORRECTA\n")
        elif saldo < retirar :
            print("NO TIENE SALDO SUFICIENTE\n")
        else :
            saldo = saldo - retirar
            print("DINERO RETIRADO CON EXITO\n")
    else :
        print("ELIGA UNA OPCION VALIDA\n")