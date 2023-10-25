from googletrans import Translator
from menu import user1_language, user2_language

def main():
    translator = Translator()
    language_user1 = user1_language
    language_user2 = user2_language

    while True:
        message_user1 = input("Usuario 1: ")
        if language_user1 != language_user2:
            translated_message = translator.translate(message_user1, dest=language_user2)
            print(f"Usuario 1 ({language_user1} -> {language_user2}): {message_user1}")
            print(f"Usuario 2: {translated_message.text}")
        else:
            print("Usuario 2: " + message_user1)

        message_user2 = input("Usuario 2: ")
        if language_user2 != language_user1:
            translated_message = translator.translate(message_user2, dest=language_user1)
            print(f"Usuario 2 ({language_user2} -> {language_user1}): {message_user2}")
            print(f"Usuario 1: {translated_message.text}")
        else:
            print("Usuario 1: " + message_user2)

if __name__ == "__main__":
    main()