from mtranslate import translate
from time import sleep
from translator import chat
from constants import *
import langdetect

clear_screen()

def main():
    user_language = input(f"Welcome to {YELLOW}Instant Translator{RESET}! What language do you speak? (es/en/fr/de):")
    clear_screen()
    username = input(translate("\n¡Hola!, ingresa tu nombre para continuar: ", to_language=user_language))
    user1_language = input(translate(f"¿Qué idioma habla el usuario 1? (es/en/fr/de): ", to_language=user_language))
    user2_language = input(f"¿Qué idioma habla el usuario 2? (es/en/fr/de): ")
    
    while True:
        def display_menu():
            clear_screen()
            default_menu = (
            f"\nBienvenido {CYAN}{username}{RESET} a {YELLOW}Instant Translator{RESET}!, por favor, selecciona una opción."
            "\n================================="
            "\n1. Iniciar chat"
            "\n2. Salir"
            "\n=================================")
    
            translated_menu = translate(default_menu, to_language=user_language)
            translated_menu = translated_menu.replace(f"{translate(CYAN, to_language=user_language)}", CYAN)
            translated_menu = translated_menu.replace(f"{translate(RESET, to_language=user_language)}", RESET)
            translated_menu = translated_menu.replace(f"{translate(YELLOW, to_language=user_language)}", YELLOW)
            print(translated_menu)
            
        display_menu()
        choice = input(translate(f"Opción: ", to_language=user_language))

        if choice == "1":
            clear_screen()
            print(translate(f"Iniciando chat con idioma de Usuario 1: {user1_language}", to_language=user_language))
            print(translate(f"Iniciando chat con idioma de Usuario 2: {user2_language}", to_language=user_language))
            sleep(2)
            clear_screen()
            chat(username, user1_language, user2_language)
            
        elif choice == "2":
            print(translate("Gracias por usar Instant Translator. ¡Hasta luego!", to_language=user_language))
            break
        
        else:
            print(translate("Opción no válida. Por favor, elija una opción válida.", to_language=user_language))


if __name__ == "__main__":
    main()
