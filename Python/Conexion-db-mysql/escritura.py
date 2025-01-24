import mysql.connector

try:
    # Conexión a la base de datos
    unsij_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="unsij",
        ssl_disabled=True
    )

    # Crear el cursor
    cursor = unsij_db.cursor()

    # Consulta SQL para insertar datos
    sql_query = "INSERT INTO alumnos(nombre_completo, matricula, id_grupo) VALUES (%s, %s, %s)"
    values = ("Prueba", "123", "2")

    # Ejecutar la consulta
    cursor.execute(sql_query, values)

    # Confirmar los cambios
    unsij_db.commit()

    # Mensaje de éxito
    print("Datos insertados exitosamente")

    # Cerrar el cursor y la conexión
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'unsij_db' in locals() and unsij_db.is_connected():
        unsij_db.close()

except mysql.connector.Error as err:
    # Manejo de errores
    print(f"Error: {err}")