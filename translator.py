from mtranslate import translate

def chat(username, user1_language, user2_language):
    while True:
        message_user1 = input(f"{username}: ({user1_language} -> {user2_language}): ")
        if user1_language != user2_language:
            translated_message = translate(message_user1, to_language=user2_language)
            print(f"Mensaje traducido al usuario 2: {translated_message}")
        else:
            print("Usuario 2: " + message_user1)

        message_user2 = input(f"Usuario 2: ({user2_language} -> {user1_language}): ")
        if user2_language != user1_language:
            translated_message = translate(message_user2, to_language=user1_language)
            print(f"Mensaje traducido al usuario 1: {translated_message}")
        else:
            print("Usuario 1: " + message_user2)