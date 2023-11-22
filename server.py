import socket, threading
from translator import translate_message


host = "127.0.0.1"
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen()

clients = []
userNames = []
userLanguages = []


# Esta funcion envia el mensaje a todos los usuarios conectados, excepto al que lo envia
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            message = translate_message(
                message.decode("utf-8"), userLanguages[clients.index(client)]
            ).encode("utf-8")
            client.send(message)


# Esta funcion maneja los mensajes de los usuarios


def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            userName = userNames[index]
            userLanguage = userLanguages[index]
            broadcast(f"{userName} left the chat".encode("utf-8"), client)
            clients.remove(client)
            userNames.remove(userName)
            userLanguages.remove(userLanguage)

            client.close()
            break


# Esta funcion recibe las conexiones de los usuarios


def receive_connections():
    while True:
        client, address = sock.accept()

        client.send("USER".encode("utf-8"))
        userName = client.recv(1024).decode("utf-8")
        client.send("LANG".encode("utf-8"))
        userLanguage = client.recv(1024).decode("utf-8")

        # Toma el nombre del usuario y el lenguaje y los agrega a las listas de usuarios conectados
        clients.append(client)
        userNames.append(userName)
        userLanguages.append(userLanguage)

        print(
            f'User: {userName}, language: "{userLanguage}" connected with {str(address)}'
        )

        message = f"{userName} joined the chat".encode("utf-8")
        broadcast(message, client)
        client.send("Connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()


receive_connections()
