
print("BIENVENIDO A MI CALCULADORA BÁSICA")
print("Escribe el número de la operación que deseas usar:")

try:
    operacion = int(input("1. SUMA  2. RESTA  3. MULTIPLICACIÓN  4. DIVISIÓN :"))

    if operacion in [1, 2, 3, 4]:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        resultado = None  

        if operacion == 1:
            resultado = numero1 + numero2
        elif operacion == 2:
            resultado = numero1 - numero2
        elif operacion == 3:
            resultado = numero1 * numero2
        elif operacion == 4:
            if numero2 == 0:
                print("NO PUEDES DIVIDIR ENTRE 0")
            else:
                resultado = numero1 / numero2

        if resultado is not None:
            print("EL RESULTADO ES:", resultado)

    else:
        print(" LA OPERACIÓN NO EXISTE.")

except ValueError:
    print("X ERROR: DEBES INGRESAR UN NÚMERO DE UNA OPERACIÓN")
