def mostrar_menu_vuelos():
    print("Vuelos")
    print("¡Elige uno de nuestros asombrosos destinos!")
    print("** VUELOS NACIONALES **")
    print("1. Chetumal")
    print("2. CDMX (Aeropuerto Internacional Benito Juárez)")
    print("3. Acapulco")
    print("4. Cancún")
    print("5. Oaxaca")
    print("** VUELOS INTERNACIONALES **")
    print("6. Dublín")
    print("7. Giza")
    print("8. Londres")
    print("9. Barcelona")
    print("10. Lima")
    print("11. Salir")

# Diccionario con los precios de ida y vuelta para cada destino (precios aproximados)
precios_vuelos = {
    "1": {"nombre": "Chetumal", "ida": 1200, "redondo": 2200},
    "2": {"nombre": "CDMX", "ida": 1500, "redondo": 2800},
    "3": {"nombre": "Acapulco", "ida": 1400, "redondo": 2600},
    "4": {"nombre": "Cancún", "ida": 1600, "redondo": 3000},
    "5": {"nombre": "Oaxaca", "ida": 1300, "redondo": 2400},
    "6": {"nombre": "Dublín", "ida": 12000, "redondo": 22000},
    "7": {"nombre": "Giza", "ida": 14000, "redondo": 26000},
    "8": {"nombre": "Londres", "ida": 15000, "redondo": 28000},
    "9": {"nombre": "Barcelona", "ida": 16000, "redondo": 30000},
    "10": {"nombre": "Lima", "ida": 11000, "redondo": 20000}
}


precios_paquetes = {
    "Zero": 0,
    "Básica": 500,
    "Premium": 1500
}

# Tarifa de Uso Aeroportuario (TUA)
TUA = 499  # Esta tarifa es aproximada y puede variar

# Bucle del menú
while True:
    mostrar_menu_vuelos()
    opcion = input("Ingrese el número de la opción que desea seleccionar: ")

    if opcion in precios_vuelos:
        destino = precios_vuelos[opcion]["nombre"]
        print("\nHas seleccionado:", destino)

        # Preguntar número de boletos
        boletos = int(input("Ingrese el número de boletos (solo adultos): "))

        # Preguntar si es solo ida o viaje redondo
        tipo_viaje = input("¿Es viaje redondo o solo de ida? (Ingrese 'redondo' o 'ida'): ").lower()
        if tipo_viaje == "redondo":
            precio_base = precios_vuelos[opcion]["redondo"]
        elif tipo_viaje == "ida":
            precio_base = precios_vuelos[opcion]["ida"]
        else:
            print("Opción de viaje no válida. Seleccionando viaje de ida por defecto.")
            precio_base = precios_vuelos[opcion]["ida"]

        # Seleccionar paquete
        print("\nSeleccione un paquete:")
        print("1. Zero (Incluye el boleto y un objeto personal de mano)")
        print("2. Básica (Incluye objeto personal de mano, equipaje de mano, además del boleto)")
        print("3. Premium (Incluye objeto personal de mano, equipaje de mano, maleta de 25kg documentada y preferencia al abordaje)")
        paquete_opcion = input("Ingrese el número del paquete (1, 2 o 3): ")

        if paquete_opcion == "1":
            paquete = "Zero"
        elif paquete_opcion == "2":
            paquete = "Básica"
        elif paquete_opcion == "3":
            paquete = "Premium"
        else:
            print("Opción de paquete no válida. Seleccionando 'Zero' por defecto.")
            paquete = "Zero"

        # Calcular el precio total
        precio_paquete = precios_paquetes[paquete]
        total_sin_tua = (precio_base + precio_paquete) * boletos
        total_con_tua = total_sin_tua + TUA

        # Mostrar resumen y total a pagar
        print("\nResumen de su selección:")
        print("Destino:", destino)
        print("Tipo de viaje:", "Redondo" if tipo_viaje == "redondo" else "Solo de ida")
        print("Paquete:", paquete)
        print("Cantidad de boletos:", boletos)
        print("Precio total (sin TUA):", "$" + str(total_sin_tua))
        print("Tarifa de Uso Aeroportuario (TUA):", "$" + str(TUA))
        print("Total a pagar:", "$" + str(total_con_tua), "\n")

    elif opcion == "11":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor seleccione una opción entre 1 y 11.")
