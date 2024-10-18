#Kevin Rafael Díaz López

print("** \tComunidad UNSIJ")

estudiante = input("¿Es estudiante de la UNSIJ? ")
estudiante = estudiante.lower() == "si"

profesor = input("¿Es profesor de la UNSIJ? ")
profesor = profesor.lower() == "si"

print(f"¿Pertenece a la comunidad UNSIJ? {estudiante or profesor}")
