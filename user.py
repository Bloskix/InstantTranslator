import socket

host = "127.0.0.1"
port = 8080

sock = socket.socket()
sock.connect((host, port))
data = sock.recv(4096)
print(data.decode('utf-8'))

while True:
    message = input("Envía un mensaje: ") #TODO: Que diferencie los usuarios, los cuales pueden estar guardados en una base de datos o más simple, en un archivo de texto.
    message += "\n"  # Agrega un salto de línea al final del mensaje
    sock.send(message.encode('utf-8'))
    if message == "quit\n":
        break
print("Adiós")
sock.close()
