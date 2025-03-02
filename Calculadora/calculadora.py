def mostrarMenu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error, no se puede dividir por 0"
    return a / b

while True:
    mostrarMenu()
    opcion = input("Ingrese una opcion (1 al 5): ")
    resultado = 0

    if opcion == "5":
        print("Hasta luego")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Ingrese una opcion valida")
        continue

    try:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
    except:
        print("Ingrese un numero valido")
        continue

    if opcion == "1":
        resultado = sumar(num1, num2)
        print(f"Resultado = {resultado}")
    elif opcion == "2":
        resultado = restar(num1, num2)
        print(f"Resultado = {resultado}")
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
        print(f"Resultado = {resultado}")
    elif opcion == "4":
        resultado = dividir(num1, num2)
        if isinstance(resultado, str):
            print(resultado)
        else:
            print(f"Resultado = {resultado}")