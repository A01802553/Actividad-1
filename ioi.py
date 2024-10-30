def mostrar_destinos():
    print("\n¡Elige uno de nuestros asombrosos destinos!")
    print("1. Chetumal")
    print("2. Ciudad de México")
    print("3. Acapulco")

def mostrar_paquetes():
    print("\n¡Elige entre nuestros paquetes!")
    print("****CLASE TURISTA****")
    print("1. SencillaAW: Artículo personal y Equipaje de mano (10kg max). Sin asiento asignado.")
    print("2. VintageAW: Artículo personal, Equipaje de Mano (15kg max), Equipaje documentado. Asiento asignado.")
    print("***LUXURY CLASS***")
    print("3. PremiumAW: Artículo personal, Equipaje de Mano (15kg max), Equipaje documentado, Comida a bordo. Asiento asignado.")

def mostrar_tipos_vuelo():
    print("\n**VUELO REDONDO O DE IDA**")
    print("1. Vuelo Redondo")
    print("2. Vuelo de Ida")

def calcular_total(tua, precio_base, num_boletos):
    return tua + (precio_base * num_boletos)

def resumen_compra(destino, paquete, tipo_vuelo, precio_base, tua, num_boletos):
    print("\n********** RESUMEN DE COMPRA **********")
    print(f"DESTINO: {destino}")
    print(f"PAQUETE: {paquete}")
    print(f"TIPO DE VUELO: {'Redondo' if tipo_vuelo == 1 else 'De ida'}")
    print(f"PRECIO BASE POR BOLETO: ${precio_base}")
    print(f"TUA (Tarifa de Uso de Aeropuerto): ${tua}")
    print(f"NÚMERO DE BOLETOS: {num_boletos}")
    total = calcular_total(tua, precio_base, num_boletos)
    print(f"TOTAL A PAGAR: ${total}")
    print("GRACIAS POR VOLAR CON AZTECA WINGS")

def elegir_destino():
    mostrar_destinos()
    while True:
        try:
            destino = int(input("Escribe el número del destino que quieras: "))
            if destino in [1, 2, 3]:
                return destino
            else:
                print("Opción no válida, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def elegir_paquete():
    mostrar_paquetes()
    while True:
        try:
            paquete = int(input("Elige el número de paquete: "))
            if paquete in [1, 2, 3]:
                return paquete
            else:
                print("Opción no válida, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def elegir_tipo_vuelo():
    mostrar_tipos_vuelo()
    while True:
        try:
            tipo_vuelo = int(input("Elige el número del tipo de vuelo: "))
            if tipo_vuelo in [1, 2]:
                return tipo_vuelo
            else:
                print("Opción no válida, intenta de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def main():
    print("********** AZTECA WINGS **********")
    print("¡Elevamos tus sueños y los llevamos a tu destino!")

    while True:
        destino = elegir_destino()
        
        # Precios por destino (indexados según destino: 1 = Chetumal, 2 = CDMX, 3 = Acapulco)
        precios_destinos = {
            1: {"nombre": "Chetumal", "SencillaAW": [2499, 450], "VintageAW": [5499, 450], "PremiumAW": [8299, 450]},
            2: {"nombre": "Ciudad de México", "SencillaAW": [2499, 650], "VintageAW": [4699, 650], "PremiumAW": [8199, 650]},
            3: {"nombre": "Acapulco", "SencillaAW": [2499, 850], "VintageAW": [3699, 850], "PremiumAW": [6299, 850]}
        }

        paquete = elegir_paquete()
        tipo_vuelo = elegir_tipo_vuelo()
        num_boletos = int(input("¿Cuántos boletos deseas comprar?: "))

        paquetes = ["SencillaAW", "VintageAW", "PremiumAW"]
        paquete_seleccionado = paquetes[paquete - 1]

        # Obtener los precios correspondientes al destino y paquete seleccionados
        precio_base, tua = precios_destinos[destino][paquete_seleccionado]

        resumen_compra(
            precios_destinos[destino]["nombre"], 
            paquete_seleccionado, 
            tipo_vuelo, 
            precio_base, 
            tua, 
            num_boletos
        )

        opcion = input("¿Deseas volver al menú principal? (Si = 1, No = 2): ")
        if opcion != "1":
            break

if __name__ == "__main__":
    main()
2