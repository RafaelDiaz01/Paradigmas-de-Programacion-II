import socket

# Crear el socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectarse al servidor
host = '127.0.0.1'  # Dirección del servidor
port = 12345        # Puerto del servidor
client_socket.connect((host, port))

# Enviar un mensaje al servidor
message = "Hola desde el cliente"
client_socket.send(message.encode())

# Recibir la respuesta del servidor
response = client_socket.recv(1024).decode()
print(f"Respuesta del servidor: {response}")

# Cerrar el socket
client_socket.close()
