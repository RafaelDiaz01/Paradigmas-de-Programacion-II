import socket

# Crear el socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enlazar el socket a una dirección y puerto
host = '127.0.0.1'  # Dirección local
port = 12345        # Puerto
server_socket.bind((host, port))

# Poner el socket en modo escucha
server_socket.listen(1)
print(f"Esperando conexiones en {host}:{port}...")

# Aceptar una conexión entrante
conn, addr = server_socket.accept()
print(f"Conexión establecida con: {addr}")

# Recibir datos
data = conn.recv(1024).decode()  # Tamaño máximo: 1024 bytes
print(f"Mensaje recibido: {data}")

# Responder al cliente
response = "Mensaje recibido con éxito"
conn.send(response.encode())

# Cerrar la conexión
conn.close()
server_socket.close()
