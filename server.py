import socket, threading

host = "127.0.0.1"
port = 8080

import socket
import threading

host = "127.0.0.1"
port = 6666

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado")
sock.bind((host, port))
print("Socket vinculado")
sock.listen(2)
print("Socket ahora escuchando")

clients = {}

def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('Conexión con {}.'.format(addr))
        conn.send("Servidor: Hola cliente".encode('UTF-8'))
        id_clients = threading.current_thread().getName() # Obtiene el nombre del hilo actual
        clients[id_clients] = conn # Agrega el socket conectado a la lista de clientes
        while True:
            data = conn.recv(4096)
            if data:
                print('Recibido de {}: {}'.format(id_clients, data.decode('utf-8')))
                for id_clients_destino, cliente_destino in clients.items():
                    if id_clients_destino != id_clients: # No envía el mensaje al cliente que lo envió
                        cliente_destino.send(data)
            else:
                print("Prueba")
                break
    finally:
        conn.close()

while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr), name=str(threading.active_count())).start() # Crea un nuevo hilo para manejar la conexión
