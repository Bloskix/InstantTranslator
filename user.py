import socket

host = "127.0.0.1"
port = 8080

sock = socket.socket()
sock.connect((host, port))
data = sock.recv(4096)
print(data.decode('utf-8'))

while True:
    mensaje = input("Envía un mensaje: ")
    mensaje += "\n"  # Agrega un salto de línea al final del mensaje
    sock.send(mensaje.encode('utf-8'))
    if mensaje == "quit\n":
        break
print("Adiós")
sock.close()
