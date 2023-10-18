import socket, threading

host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)
print("Servidor escuchando en {}:{}...".format(host, port))

def worker(*args):
    conn = args[0]
    addr = args[1]
    try:
        print('Conexión con {}.'.format(addr))
        conn.send("Servidor: Hola cliente".encode('UTF-8'))
        while True:
            datos = conn.recv(4096)
            if datos:
                print('Recibido: {}'.format(datos.decode('utf-8')))
            else:
                print("Prueba")
                break
    finally:
        conn.close()

while 1:
    conn, addr = sock.accept()
    threading.Thread(target=worker, args=(conn, addr)).start()
