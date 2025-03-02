#el INPUT es para que el usuario pueda ingresar un valor

print ("BIENVENIDOS A MI CALCULADORA BÁSICA")

nombre = input("¿Cuál es tu nombre?: ")
print ("Hola,", nombre)

numero1 = input("Ingresa el primer número para realizar una suma: ")
numero2 = input("Ingresa el segundo número para realizar una suma: ")

numero1 = int(numero1)
numero2 = int(numero2)

resultado= numero1 + numero2

resultado = str(resultado)

print("LA RESPUESTA DE LA SUMA ES:", resultado)

print("A continuación las demás operaciones segun los números que ingresaste:")

resultado2 = numero1 * numero2
resultado3 = numero1 - numero2

resultado2 = str(resultado2)
resultado3 = str(resultado3)

print("LA MULTIPLICACIÓN DE LOS NUMEROS ES:", resultado2)
print("LA RESTA DE LOS NUMEROS ES:", resultado3)

print ("GRACIAS POR UTILIZAR MI CALCULADORA BÁSICA")

