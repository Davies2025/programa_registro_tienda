
print ("BIENVENIDO A MI CALCULADORA BÁSICA")

print ("Escribe el número de la operación que deseas usar:")

operacion = int(input("1.SUMA 2.RESTA 3.Multiplicación 4.División "))

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

if operacion == 1: 
    resultado1 = numero1 + numero2 
    print (resultado1)

elif operacion == 2:
    resultado2 = numero1 - numero2 
    print (resultado2)

elif operacion == 3:
    resultado3 = numero1 * numero2 
    print (resultado3)

elif operacion == 4:
    resultado4 = numero1 / numero2 
    print (resultado4)

