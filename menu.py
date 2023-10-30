from googletrans import Translator
from time import sleep
from translator import chat
from constants import *

clear_screen()

translator = Translator()
username = input("¡Bienvenido a Instant Translator!\nIngresa tu nombre para continuar: ")
user1_language = ""
user2_language = ""

clear_screen()

def display_menu():
    print(f"\nBienvenido {CYAN}{username}{RESET}, selecciona una opción: ") #TODO: Mejorar la estética, facilitar la experiencia de usuario.
    print("=================================")
    print("1. Seleccionar idioma para Usuario 1")
    print("2. Seleccionar idioma para Usuario 2")
    print("3. Iniciar chat")
    print("4. Salir")
    print("=================================")

def main():
    while True:
        display_menu()
        choice = input(f"{username}, seleccione una opción: ")

        if choice == "1":
            user1_language = input(f"¿Qué idioma hablas? (es/en/fr/de): ")
        elif choice == "2":
            user2_language = input(f"¿Qué idioma hablas? (es/en/fr/de): ")
        elif choice == "3":
            clear_screen()
            print(f"Iniciando chat con idioma de Usuario 1: {user1_language}")
            print(f"Iniciando chat con idioma de Usuario 2: {user2_language}")
            sleep(2)
            clear_screen()
            chat(username, user1_language, user2_language)
        elif choice == "4":
            print("Gracias por usar Instant Translator. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
