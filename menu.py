from googletrans import Translator
from translator import chat
from constants import *

clear_screen()

translator = Translator()
client = input("¡Bienvenido a Instant Translator!\nIngresa tu nombre para continuar: ")
client_lang = input(f"¿Qué idioma hablas? (es/en/fr/de): ") #TODO: Que cada usuario tenga un idioma diferente y probar con otros idiomas menos comúnes.

clear_screen()

def display_menu():
    print(f"\nBienvenido {CYAN}{client}{RESET}, selecciona una opción: ") #TODO: Mejorar la estética, facilitar la experiencia de usuario.
    print("=================================")
    print("1. Establecer idioma para Usuario 1")
    print("2. Establecer idioma para Usuario 2")
    print("3. Iniciar chat")
    print("4. Salir")
    print("=================================")

def main():
    user1_language = "es"
    user2_language = "en"

    while True:
        display_menu()
        choice = input(f"{client}, seleccione una opción: ")

        if choice == "1":
            user1_language = input(f"¿Qué idioma hablas? (es/en/fr/de): ")
        elif choice == "2":
            user2_language = input(f"¿Qué idioma hablas? (es/en/fr/de): ")
        elif choice == "3":
            print(f"Iniciando chat con idioma de Usuario 1: {user1_language}")
            print(f"Iniciando chat con idioma de Usuario 2: {user2_language}")
            chat()
        elif choice == "4":
            print("Gracias por usar Instant Translator. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
