import os, subprocess


# Clear screen
def clear_screen():
    os.system("cls")


# Run server
def run_server():
    os.chdir(r".")
    subprocess.Popen(["start", "cmd", "/k", "py server.py"], shell=True)
    print("Servidor ejecutado correctamente.")
    # try:
    #     subprocess.Popen(["start", "cmd", "/k", "python3 server.py"], shell=True)
    #     print("Servidor ejecutado correctamente.")
    # except Exception:
    #     try:
    #         subprocess.Popen(["start", "cmd", "/k", "py server.py"], shell=True)
    #         print("Servidor ejecutado correctamente.")
    #     except FileNotFoundError:
    #         print("No se pudo ejecutar el servidor.")


# Colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
RESET = "\033[0m"

# Languages
LANGUAGES = ["es", "en", "fr", "de"]
