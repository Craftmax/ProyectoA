# utils.py

def helper_function():
    """
    Realiza una operación útil y devuelve un mensaje.
    """
    return "¡Bienvenido a las funciones útiles del proyecto!"

def generate_greeting(name):
    """
    Genera un saludo personalizado utilizando el nombre proporcionado.
    """
    return f"Hola, {name}! Gracias por ser parte de este proyecto."

def calculate_average(numbers):
    """
    Calcula el promedio de una lista de números.
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

# Puedes agregar más funciones de utilidad según sea necesario