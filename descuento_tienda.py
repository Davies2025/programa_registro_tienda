print ("BIENVENIDO A LA TIENDA PYTHON_SQL")

print ("Selecciona el Área de dondé quieres el descuento:")

try:

    area = int(input("1. Frutas 2. Carnes 3. Lácteos 4. Juguetes "))
    
    
    descuento = None
    
    
    if area in [1, 2, 3, 4]:

        precio = float(input("Ingresa el precio del producto: "))
    
        if area == 1: 
            if precio <= 0:
                print ("No hay descuento, el precio es 0 o NEGATIVO")
            else: 
                descuento = precio * 0.10
        elif area == 2: 
             if precio <= 0:
                print ("No hay descuento, el precio es 0 o NEGATIVO")
             else: 
                descuento = precio * 0.15
        elif area == 3:
            if precio <= 0:
                print ("No hay descuento, el precio es 0 o NEGATIVO")
            else: 
                descuento = precio * 0.20
        elif area == 4:
            if precio <= 0:
                print ("No hay descuento, el precio es 0 o NEGATIVO")
            else: 
                descuento = precio * 0.25
        if descuento is not None: 
            print ("El descuento es:", descuento)

    else: 
        print ("La Área NO EXISTE")

except ValueError:
    print("X ERROR")