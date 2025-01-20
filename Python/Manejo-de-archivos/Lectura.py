# Kevin Rafael Díaz López - 14/01/2025
# w = write, a = append , encoding = "utf-8" (para reconocer acentos), para lectura es r o no poner nada ya que
# lectura es por default

try:
    archivo = open("Rifa_archivos.py", "r")
    lectura_archivo = archivo.read()
    print(lectura_archivo)
except FileNotFoundError as e:
    print(f"El archivo no está en esa ruta | {e}")