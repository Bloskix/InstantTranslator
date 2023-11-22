from mtranslate import translate
from time import sleep
from constants import *
from client import *


def main():
    clear_screen()
    userLanguage = input(
        f"Welcome to {YELLOW}Instant Translator{RESET}! What language do you speak? (es/en/fr/de):"
    )
    while userLanguage not in LANGUAGES:
        print(f"{RED}Invalid language. Please, enter a valid language.{RESET}")
        userLanguage = input(f"What language do you speak? (es/en/fr/de):")
    clear_screen()
    userName = input(
        translate(
            "\n¡Hola!, ingresa tu nombre para continuar: ", to_language=userLanguage
        )
    )

    while True:

        def display_menu():
            clear_screen()
            defaultMenu = (
                f"\nBienvenido {CYAN}{userName}{RESET} a {YELLOW}Instant Translator{RESET}!, por favor, selecciona una opción."
                "\n================================="
                "\n1. Crear sala de chat"
                "\n2. Unirse a sala de chat"
                "\n3. Cambiar idioma"
                f"\n{RED}4. Salir{RESET}"
                "\n================================="
            )

            colors = [CYAN, YELLOW, RED, RESET]
            translatedMenu = translate(defaultMenu, to_language=userLanguage)

            for color in colors:
                translatedMenu = translatedMenu.replace(
                    translate(color, to_language=userLanguage), color
                )

            print(translatedMenu)

        display_menu()
        choice = input(translate(f"Opción: ", to_language=userLanguage))

        if choice == "1":
            clear_screen()
            run_server()
            if not run_client(userName, userLanguage):
                continue
            break
        elif choice == "2":
            clear_screen()
            if not run_client(userName, userLanguage):
                continue
            break

        elif choice == "3":
            clear_screen()
            userLanguage = input(
                translate(
                    "\nElije tu nuevo idioma para continuar (es/en/fr/de): ",
                    to_language=userLanguage,
                )
            )
            while userLanguage not in LANGUAGES:
                print(
                    f"{RED}Idioma no válido. Por favor, ingrese un idioma válido.{RESET}"
                )
                userLanguage = input(
                    f"Elije tu nuevo idioma para continuar (es/en/fr/de): "
                )

        elif choice == "4":
            clear_screen()
            sleep(1)
            print(
                translate(
                    "Gracias por usar Instant Translator. ¡Hasta luego!",
                    to_language=userLanguage,
                )
            )
            sleep(1)
            break

        else:
            print(
                translate(
                    "Opción no válida. Por favor, elija una opción válida.",
                    to_language=userLanguage,
                )
            )


if __name__ == "__main__":
    main()
