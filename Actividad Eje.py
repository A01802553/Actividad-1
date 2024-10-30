print(" Azteca Wings") 
print("Elevamos tu sueños y los llevamos a tu destino")
print(" ¡Elige uno de nuestros asombros destinos! ")
print(" ** 1.....Chetumal** ")
print(" ** 2......Ciudad Mexico** ")
print(" ** 3......Acapulco**")

wh = (int(input("Presione 1 para continuar..")))


while wh == 1:

 print(" Azteca Wings") 
 print("Elevamos tu sueños y los llevamos a tu destino")
 print(" ¡Elige uno de nuestros asombros destinos! ")
 print(" ** 1.....Chetumal** ")
 print(" ** 2......Ciudad Mexico** ")
 print(" ** 3......Acapulco**")

 dst = int(input("Escribe el número del destino que quieras")) 
 if dst == 1:
    print ("Haz elegido Chetumal")
    print ("¡Elige entre nuestros paquetes!")
    print ("****CLASE TURISTA****")
    print ("1.SencillaAW: Incluye un Artículo personal  y un Equipaje de mano (10kg max.). Sin asiento asignado")
    print ("2.VintageAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + EquipaJe documentado. Asiento asignado ")
    print ("***LUXURY CLASS***")
    print ("3.PremiumAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) +  EquipaJe documentado + Comida durante el vuelo + Mas comodidad :). Asiento asignado")
    aw1= int(input("Elige el numero de paquete"))     

    if aw1 == 1:
        print ("Haz elegido el Paquete SencilloAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 450
            chvr = 4499
            print ("Haz elegido VUELO REDONDO.....$4499 sin TUA")
            print ("Este paquete no incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CHETUMAL")
            print ("PAQUETE................SENCILLOAW........$4999")
            print ("TUA......................................$450")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 450
            chvr = 2499
            print ("Haz elegido VUELO de Ida.....$2499 sin TUA")
            print ("Este paquete no incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CHETUMAL")
            print ("PAQUETE................SENCILLOAW........$2499")
            print ("TUA......................................$450")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")

    elif aw1 == 2:
        print ("Haz elegido el Paquete VintageAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 450
            chvr = 8299
            print ("Haz elegido VUELO REDONDO.....$8299 sin TUA")
            print ("Este paquete  incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CHETUMAL")
            print ("PAQUETE................VINTAGEAW........$8299")
            print ("TUA......................................$450")

            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 450
            chvr = 5499
            print ("Haz elegido VUELO de Ida.....$5499 sin TUA")
            print ("Este paquete incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CHETUMAL")
            print ("PAQUETE................VINTAGEAW........$5499")
            print ("TUA......................................$450")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")
    
    elif aw1 == 3:
        print ("Haz elegido el Paquete PremiunmAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 450
            chvr = 8299
            print ("Haz elegido VUELO REDONDO.....$8299 sin TUA")
            print ("Este paquete  incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CHETUMAL")
            print ("PAQUETE................PREMIUMAW........$8299")
            print ("TUA......................................$450")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 450
            chvr = 5499
            print ("Haz elegido VUELO de Ida.....$5499 PremiumAW")
            print ("Este paquete incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CHETUMAL")
            print ("PAQUETE................PREMIUMAW........$5499")
            print ("TUA......................................$450")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")

 if dst == 2:
    print ("Haz elegido CDMX")
    print ("¡Elige entre nuestros paquetes!")
    print ("****CLASE TURISTA****")
    print ("1.SencillaAW: Incluye un Artículo personal  y un Equipaje de mano (10kg max.). Sin asiento asignado")
    print ("2.VintageAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + EquipaJe documentado. Asiento asignado ")
    print ("***LUXURY CLASS***")
    print ("3.PremiumAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) +  EquipaJe documentado + Comida durante el vuelo + Mas comodidad :). Asiento asignado")
    aw1= int(input("Elige el numero de paquete"))     

    if aw1 == 1:
        print ("Haz elegido el Paquete SencilloAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 650
            chvr = 3299
            print ("Haz elegido VUELO REDONDO.....$3299 sin TUA")
            print ("Este paquete no incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CDMX")
            print ("PAQUETE................SENCILLOAW........$3299")
            print ("TUA......................................$650")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 650
            chvr = 2499
            print ("Haz elegido VUELO de Ida.....$2499 sin TUA")
            print ("Este paquete no incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CDMX")
            print ("PAQUETE................SENCILLOAW........$2499")
            print ("TUA......................................$650")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")

    elif aw1 == 2:
        print ("Haz elegido el Paquete VintageAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 650
            chvr = 7299
            print ("Haz elegido VUELO REDONDO.....$7299 sin TUA")
            print ("Este paquete  incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CDMX")
            print ("PAQUETE................VINTAGEAW........$7299")
            print ("TUA......................................$650")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 650
            chvr = 4699
            print ("Haz elegido VUELO de Ida.....$4699 sin TUA")
            print ("Este paquete incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CDMX")
            print ("PAQUETE................VINTAGEAW........$4699")
            print ("TUA......................................$650")

            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")
    
    elif aw1 == 3:
        print ("Haz elegido el Paquete PremiunmAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 450
            chvr = 8199
            print ("Haz elegido VUELO REDONDO.....$8199 sin TUA")
            print ("Este paquete  incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CDMX")
            print ("PAQUETE................PREMIUMAW........$8199")
            print ("TUA......................................$650")

            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 650
            chvr = 4399
            print ("Haz elegido VUELO de Ida.....$4399 PremiumAW")
            print ("Este paquete incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................CDMX")
            print ("PAQUETE................PREMIUMAW........$4399")
            print ("TUA......................................$650")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")        

 if dst == 3:
    print ("Haz elegido Acapulco")
    print ("¡Elige entre nuestros paquetes!")
    print ("****CLASE TURISTA****")
    print ("1.SencillaAW: Incluye un Artículo personal  y un Equipaje de mano (10kg max.). Sin asiento asignado")
    print ("2.VintageAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) + EquipaJe documentado. Asiento asignado ")
    print ("***LUXURY CLASS***")
    print ("3.PremiumAW: Incluye un Artículo personal + un Equipaje de Mano (15kg max.) +  EquipaJe documentado + Comida durante el vuelo + Mas comodidad :). Asiento asignado")
    aw1= int(input("Elige el numero de paquete"))     

    if aw1 == 1:
        print ("Haz elegido el Paquete SencilloAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 850
            chvr = 4199
            print ("Haz elegido VUELO REDONDO.....$4199 sin TUA")
            print ("Este paquete no incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................ACAPULCO")
            print ("PAQUETE................SENCILLOAW........$4199")
            print ("TUA......................................$850")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 850
            chvr = 2499
            print ("Haz elegido VUELO de Ida.....$2499 sin TUA")
            print ("Este paquete no incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................ACAPULCO")
            print ("PAQUETE................SENCILLOAW........$2499")
            print ("TUA......................................$850")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")

    elif aw1 == 2:
        print ("Haz elegido el Paquete VintageAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 850
            chvr = 6299
            print ("Haz elegido VUELO REDONDO.....$6299 sin TUA")
            print ("Este paquete  incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................ACAPULCO")
            print ("PAQUETE................VINTAGEAW........$6299")
            print ("TUA......................................$850")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 850
            chvr = 3699
            print ("Haz elegido VUELO de Ida.....$3699 sin TUA")
            print ("Este paquete incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................ACAPULCO")
            print ("PAQUETE................VINTAGEAW........$3699")
            print ("TUA......................................$850")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo")
    
    elif aw1 == 3:
        print ("Haz elegido el Paquete PremiunmAW")
        print ("**VUELO REDONDO O DE IDA**")
        print ("1. Vuelo Redondo")
        print ("2. Vuelo de Ida")

        vls = int(input("Escribe el numero del tipo de vuelo que quieras"))
        if vls == 1:
            tua = 850
            chvr = 7699
            print ("Haz elegido VUELO REDONDO.....$7699 sin TUA")
            print ("Este paquete  incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))

            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................ACAPULCO")
            print ("PAQUETE................PREMINUMAW........$7699")
            print ("TUA......................................$850")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        elif vls == 2:
            tua = 850
            chvr = 5499
            print ("Haz elegido VUELO de Ida.....$4889 PremiumAW sin TUA")
            print ("Este paquete incluye maleta documentada")
            nb = (int(input("Ingresa el número de boletos que quieras")))
            print ("Presiona enter para finalizar compra")
            input()
            print ("AZTECA WINGS")
            print ("DESTINO................ACAPULCO")
            print ("PAQUETE................PREMIUMAW........$4899")
            print ("TUA......................................$850")
            print ("NUMERO DE BOLETOS........................",nb)
            total = tua + (chvr*nb)
            print ("TOTAL......................$",total)
            print (" GRACIAS POR VOLAR CON AZTECA WINGS")
            wh = (int(input("Desea volver al menú de inicio? Si.1 No.2")))
        else: 
            print("Valor incorrecto intentelo de nuevo") 
