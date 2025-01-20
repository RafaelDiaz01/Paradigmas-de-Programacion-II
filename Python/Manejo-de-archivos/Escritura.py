# Kevin Rafael Díaz López - 14/01/2025
# w = write, a = append , encoding = "utf-8" (para reconocer acentos)

try:
    archivo = open("archivo_prueba.txt", "w")
    archivo.write("Hola Rafael \n")
    archivo.write("Adiós Rafael")
except Exception as e:
    print(e)