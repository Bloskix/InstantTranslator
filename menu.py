import googletrans

def display_menu():
    print("Bienvenido a Instant Translator!")
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
        CLIENT = print(input("¡Bienvenido a Instant Translator!\nIngresa tu nombre para continuar: "))
        display_menu()
        choice = input("Seleccione una opción: ")

        if choice == "1":
            user1_language = input(f"¿Qué idioma hablas? (es/en/fr/de): ")
        elif choice == "2":
            user2_language = input(f"? (es/en/fr/de): ")
        elif choice == "3":
            print(f"Iniciando chat con idioma de Usuario 1: {user1_language}")
            print(f"Iniciando chat con idioma de Usuario 2: {user2_language}")
            googletrans()
        elif choice == "4":
            print("Gracias por usar Instant Translator. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

if __name__ == "__main__":
    main()
