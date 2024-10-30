print("Azteca Wings") 
print("Elevamos tus sueños y los llevamos a tu destino")
print("¡Elige uno de nuestros asombros destinos!")
print(" ** 1.....Chetumal** ")
print(" ** 2......Ciudad de México** ")
print(" ** 3......Acapulco**")

wh = int(input("Presione 1 para continuar..."))

while wh == 1:
    print("Azteca Wings")
    print("Elevamos tus sueños y los llevamos a tu destino")
    print("¡Elige uno de nuestros asombros destinos!")
    print(" ** 1.....Chetumal** ")
    print(" ** 2......Ciudad de México** ")
    print(" ** 3......Acapulco**")

    dst = int(input("Escribe el número del destino que quieras: ")) 

    if dst in [1, 2, 3]:
        nombre = input("Ingresa el nombre para la reservación: ")
        
        if dst == 1:
            destino = "Chetumal"
        elif dst == 2:
            destino = "Ciudad de México"
        else:
            destino = "Acapulco"
        
        print(f"Haz elegido {destino}")
        print("¡Elige entre nuestros paquetes!")
        print("****CLASE TURISTA****")
        print("1. SencillaAW: Incluye un Artículo personal y un Equipaje de mano (10kg max.). Sin asiento asignado")
        print("2. VintageAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + Equipaje documentado. Asiento asignado")
        print("***LUXURY CLASS***")
        print("3. PremiumAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + Equipaje documentado + Comida durante el vuelo. Asiento asignado")

        aw1 = int(input("Elige el número de paquete: "))     

        # Define los precios según el paquete elegido
        if aw1 == 1:
            paquete = "SencillaAW"
            incluye_maleta = False
            precio_redondo = 4500
            precio_ida = 2500
        elif aw1 == 2:
            paquete = "VintageAW"
            incluye_maleta = True
            precio_redondo = 8300
            precio_ida = 5500
        elif aw1 == 3:
            paquete = "PremiumAW"
            incluye_maleta = True
            precio_redondo = 8500
            precio_ida = 5700
        else:
            print("Paquete inválido.")
            continue
        
        print("**VUELO REDONDO O DE IDA**")
        print("1. Vuelo Redondo")
        print("2. Vuelo de Ida")
        vls = int(input("Escribe el número del tipo de vuelo que quieras: "))

        if vls == 1:
            tipo_vuelo = "Redondo"
            precio = precio_redondo
        elif vls == 2:
            tipo_vuelo = "De Ida"
            precio = precio_ida
        else:
            print("Valor incorrecto. Inténtelo de nuevo.")
            continue
        
        nb = int(input("Ingresa el número de boletos que quieras: "))

        if incluye_maleta:
            maletas = int(input(f"¿Cuántas maletas documentará para cada boleto? (Máximo permitido por paquete): "))
        else:
            maletas = 0

        tua = 450  # Impuesto TUA
        total = (precio + tua) * nb

        print("\n---------------------RESUMEN DE COMPRA---------------------")
        print(f"Nombre: {nombre}")
        print(f"Destino: {destino}")
        print(f"Paquete: {paquete}")
        print(f"Vuelo: {tipo_vuelo}")
        print(f"Maletas documentadas por boleto: {maletas}")
        print(f"Boletos: {nb}")
        print(f"TUA: ${tua}")
        print(f"Total a pagar: ${total}")
        print("GRACIAS POR VOLAR CON AZTECA WINGS")
        print("----------------------------------------------------------\n")

    else:
        print("Destino inválido.")
    
    wh = int(input("¿Desea volver al menú de inicio? Si (1) / No (2): "))
