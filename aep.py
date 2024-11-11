print("Volaris")
print("Trascender al crear y vivir las mejores experiencias de viaje.")
print("¡Elige uno de nuestros asombros destinos!")

print("** VUELOS NACIONALES **")
print("1.....Chetumal")
print("2.....Ciudad de México (CDMX)")
print("3.....Acapulco")
print("4.....Cancún")
print("5.....Oaxaca")

print("** VUELOS INTERNACIONALES **")
print("6.....Dublín")
print("7.....Giza")
print("8.....Londres")
print("9.....Barcelona")
print("10.....Lima")

wh = int(input("Presione 1 para continuar.."))

while wh == 1:
    print("\nVolaris")
    print("Trascender al crear y vivir las mejores experiencias de viaje.")
    print("¡Elige uno de nuestros asombros destinos!")

    # Mostrar opciones nacionales e internacionales
    print("** VUELOS NACIONALES **")
    print("1.....Chetumal")
    print("2.....Ciudad de México (CDMX)")
    print("3.....Acapulco")
    print("4.....Cancún")
    print("5.....Oaxaca")
    
    print("** VUELOS INTERNACIONALES **")
    print("6.....Dublín")
    print("7.....Giza")
    print("8.....Londres")
    print("9.....Barcelona")
    print("10.....Lima")

    # Selección de destino
    dst = int(input("Escribe el número del destino que quieras: "))

    # Determinar si el vuelo es nacional o internacional
    if 1 <= dst <= 5:
        print("Haz elegido un destino nacional.")
        if dst == 1:
            destino = "Chetumal"
        elif dst == 2:
            destino = "CDMX"
        elif dst == 3:
            destino = "Acapulco"
        elif dst == 4:
            destino = "Cancún"
        elif dst == 5:
            destino = "Oaxaca"
    elif 6 <= dst <= 10:
        print("Haz elegido un destino internacional.")
        if dst == 6:
            destino = "Dublín"
        elif dst == 7:
            destino = "Giza"
        elif dst == 8:
            destino = "Londres"
        elif dst == 9:
            destino = "Barcelona"
        elif dst == 10:
            destino = "Lima"
    else:
        print("Destino no válido. Por favor intenta de nuevo.")
        continue

    print(f"Haz elegido {destino}")
    print("¡Elige entre nuestros paquetes!")
    print("****CLASE TURISTA****")
    print("1. SencillaAW: Incluye un Artículo personal y un Equipaje de mano (10kg max.). Sin asiento asignado")
    print("2. VintageAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + Equipaje documentado. Asiento asignado")
    print("***LUXURY CLASS***")
    print("3. PremiumAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + Equipaje documentado + Comida durante el vuelo + Más comodidad :). Asiento asignado")

    # Selección de paquete
    aw1 = int(input("Elige el número de paquete: "))

    # Definir precios según el paquete y tipo de vuelo
    if aw1 == 1:
        paquete = "SencillaAW"
        redondo = 4499 if dst <= 5 else 8499
        ida = 2499 if dst <= 5 else 5299
    elif aw1 == 2:
        paquete = "VintageAW"
        redondo = 8299 if dst <= 5 else 12999
        ida = 5499 if dst <= 5 else 7999
    elif aw1 == 3:
        paquete = "PremiumAW"
        redondo = 9299 if dst <= 5 else 13999
        ida = 6299 if dst <= 5 else 8799
    else:
        print("Paquete no válido. Por favor intenta de nuevo.")
        continue

    print("** VUELO REDONDO O DE IDA **")
    print("1. Vuelo Redondo")
    print("2. Vuelo de Ida")

    # Selección de tipo de vuelo
    vls = int(input("Escribe el número del tipo de vuelo que quieras: "))
    tua = 450 if dst <= 5 else 850

    if vls == 1:
        tipo_vuelo = "VUELO REDONDO"
        precio = redondo
    elif vls == 2:
        tipo_vuelo = "VUELO de IDA"
        precio = ida
    else:
        print("Tipo de vuelo no válido. Por favor intenta de nuevo.")
        continue

    nb = int(input("Ingresa el número de boletos que quieras: "))
    print("Presiona enter para finalizar compra")
    input()

    print("VOLARIS")
    print(f"DESTINO................{destino}")
    print(f"PAQUETE................{paquete}........${precio}")
    print(f"TUA......................................${tua}")
    print("NUMERO DE BOLETOS........................", nb)
    total = tua + (precio * nb)
    print("TOTAL......................$", total)
    print("GRACIAS POR VOLAR CON VOLARIS")

    wh = int(input("Desea volver al menú de inicio? Si.1 No.2"))
