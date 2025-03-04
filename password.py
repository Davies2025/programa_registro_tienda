
password1 = int(input("INGRESE UNA CONTRASEÑA DE 3 DIGITOS:"))

confirmacion = int (input("CONFIRME LA CONTRASEÑA:"))

while password1 != confirmacion:
    print ("CONTRASEÑA INCORRECTA")
    confirmacion = int(input("INGRESE DE NUEVO LA CONTRASEÑA:"))
if password1 == confirmacion:
    print ("CONTRASEÑA CORRECTA")
    
print ("¡Felicidades! La contraseña es correcta.")

if password1 == confirmacion: 
    nombre = str(input("INGRESE SU NOMBRE:"))
    edad = int(input("INGRESE SU EDAD:"))
    print ("¡Felicidades!", nombre, "¡Estás registrado en la tienda!")

    opciones = int(input("¿Deseas ver los productos de la tienda? 1. Sí 2. No:"))
    if opciones == 1:
        print ("PRODUCTOS DE LA TIENDA:")
        print ("1. Frutas 2. Carnes 3. Lácteos 4. Juguetes")
        venta = int(input("¿Qué producto deseas comprar?: "))

        total = None

        if venta in [1, 2, 3, 4]:
            print ("Frutas")
            producto = float(input("¿Cuántas Manzanas deseas comprar. CADA UNA VALE $0.35?: "))
            precio = 0.35
            total = producto * precio

        elif venta == 2:
            print ("Carnes")
            producto = float(input("¿Cuántas libras de carne desea comprar. CADA UNA VALE $1.50?: "))
            precio = 1.50
            total = producto * precio

        elif venta == 3:
            print ("Lácteos")
            producto = float(input("¿Cuántas Quesos desea comprar. CADA UNO VALE $1.00?: "))
            precio = 1.00
            total = producto * precio

        elif venta == 4:
            print ("Juguetes")
            producto = float(input("¿Cuántas carritos desea comprar. CADA UNO VALE $0.75?: "))
            precio = 0.75
            total = producto * precio

        if total is not None: 
            print ("El total a pagar es:", total)
            print ("¡GRACIAS POR SU COMPRA!")

        else: 
            print ("NO SELECCIONASTE NIGUNA OPCION DE PRODUCTO")
    
    else: 
        print ("¡SALUUUUUUUUUU!")


