import socket, threading
from time import sleep
from mtranslate import translate

def run_client(userName, userLanguage): #Probar cambiar a asyncio
    host = '127.0.0.1'
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
    except socket.error as e:
        print('No se pudo conectar al servidor. \nVolviendo al menú principal.')
        sleep(2)
        return False

    def receive_messages():
        while True:
            try:
                message = client.recv(1024).decode('utf-8')
                if message == 'USER':
                    client.send(userName.encode('utf-8'))
                elif message == 'LANG':
                    client.send(userLanguage.encode('utf-8'))
                else:
                    print(message)
            except:
                print('An error ocurred!')
                client.close()
                break

    def write_messages():
        while True:
            message = f'{userName}: {input("")}'
            if message == f'{userName}: {translate("EXIT", to_language=userLanguage)}': #Crear una funcion con to_language=userLanguage
                client.close()
                break
            else:
                client.send(message.encode('utf-8'))

    recive_thread = threading.Thread(target=receive_messages)
    recive_thread.start()

    write_thread = threading.Thread(target=write_messages)
    write_thread.start()
    
    return True