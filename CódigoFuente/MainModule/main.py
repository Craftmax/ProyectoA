# main.py

from utils import helper_function
from external_library1 import library1

def user_input():
    user_name = input("Frankoxt: ")
    return user_name

def main():
    print("¡Bienvenido al ProyectoA!")

    # Obtener entrada del usuario
    name = user_input()
    print(f"Hola, {name}.")

    # Lógica principal del programa
    result = helper_function()
    print(f"Resultado de la función de ayuda: {result}")

    # Utilizando funciones de la biblioteca externa
    library1_result = library1.some_function()
    print(f"Resultado de la función de la biblioteca externa: {library1_result}")

if __name__ == "__main__":
    main()