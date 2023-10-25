from googletrans import Translator

def chat():
    translator = Translator()
    language_user1 = "es"  #TODO: Que el usuario elija su lenguaje, no hard codeado.
    language_user2 = "en" 

    while True:
        message_user1 = input(f"Usuario 1: ({language_user1} -> {language_user2}): ") #TODO: Que se detecte cuando el usuario está escribiendo con keychar.
        if language_user1 != language_user2:
            translated_message = translator.translate(message_user1, dest=language_user2)
            print(f"Mensaje traducido al usuario 2: {translated_message.text}")
        else:
            print("Usuario 2: " + message_user1) #TODO: Ver cosas como que pasa si los dos usuarios tienen el mismo idioma (que no traduzca) o que pasa si no se escribe nada.

        message_user2 = input(f"Usuario 2: ({language_user2} -> {language_user1}): ")
        if language_user2 != language_user1:
            translated_message = translator.translate(message_user2, dest=language_user1)
            print(f"Mensaje traducido al usuario 1: {translated_message.text}")
        else:
            print("Usuario 1: " + message_user2)

if __name__ == "__chat__":
    chat()