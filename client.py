import socket, threading
from mtranslate import translate

def run_client(userName, userLanguage):
    host = '127.0.0.1'
    port = 8080

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    def recive_messages():
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
            if message == f'{userName}: {translate("EXIT", to_language=userLanguage)}':
                client.close()
                break
            else:
                client.send(message.encode('utf-8'))

    recive_thread = threading.Thread(target=recive_messages)
    recive_thread.start()

    write_thread = threading.Thread(target=write_messages)
    write_thread.start()

def on_press(event):
    if event.name == 'q' and event.ctrl:
        return True