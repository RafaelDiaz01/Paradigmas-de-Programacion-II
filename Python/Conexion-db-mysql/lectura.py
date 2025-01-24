import mysql.connector

try:
    unsij_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="unsij",
        ssl_disabled=True
    )
    print("Conexión exitosa")
except mysql.connector.Error as err:
    print(f"Error: {err}")

cursor = unsij_db.cursor()
cursor.execute("SELECT  * FROM alumnos")
carreras = cursor.fetchall()

print(carreras)

unsij_db.close()
