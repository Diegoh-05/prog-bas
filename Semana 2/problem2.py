# Funciones para las operaciones
def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: No se puede dividir entre 0."

# Función principal de la calculadora
def calculadora():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Solicitar al usuario la operación
    operacion = input("Elige una operación (1/2/3/4): ")

    # Solicitar los números
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if operacion == '1':
        print(f"{num1} + {num2} = {suma(num1, num2)}")
    elif operacion == '2':
        print(f"{num1} - {num2} = {resta(num1, num2)}")
    elif operacion == '3':
        print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")
    elif operacion == '4':
        print(f"{num1} / {num2} = {division(num1, num2)}")
    else:
        print("Operación no válida")

# Llamar a la función para ejecutar la calculadora
calculadora()
