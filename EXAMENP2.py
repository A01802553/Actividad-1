print("HGMALL")
print("Bienvenido a nuestra tienda en Línea!!! :)")
print("Encuentra productos de: ")
print("1. Línea Blanca")
abc = input("¿Desea continuar? Escriba 'si' o 'no': ").lower()

# Variable para almacenar el total acumulado de la compra
total_final = 0

while abc == "si":
  
  print("Has seleccionado LINEA BLANCA")
  print("1. Refrigerador 25 Pies LG Silver $19,990.00")
  print("2. Lavadora Whirlpool 17 Kg Blanca $7,990.00")
  print("3. Estufa Mabe EM7654BFIS2 Piso 30 Plata Mercury $9,169.00")
  print("4. Licuadora Ninja Professional Blender 3 Velocidades Negra $1,890.00")
  print("5. Freidora de Aire Gourmia de 7.5 L / 8 Qt con 12 Preajustes de un Solo Toque $1,690.00")
  print("6. Horno de Microondas Whirlpool 1.1 Pies Cúbicos Silver $2,399.00")
  print("7. Batidora 2 en 1 Hamilton Beach Modelo 64650 2 en 1 Pedestal y de Mano $849.00")
  print("8. Cafetera Oster para Espresso y Cappuccino Plata con Negro $1,607.60")
  print("9. Wafflera Hamilton Beach Diseño con Acero Inoxidable Antiadherente Negro $599.00")
  print("10. Sandwichera Parrilla Hamilton Beach 25410 Antiadherente Azul $899.00")
   
  labs = int(input("Elige un producto (1-10): "))

  if labs == 1:
    print("Refrigerador 25 Pies LG Silver $19,990.00")
    nblbs = int(input("Ingresa el número de refrigeradores deseados: "))
    if nblbs >= 4:
      print("No existen tantos en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nblbs * 19990
      total_final += subtotal
      print("Has seleccionado", nblbs, "refrigerador(es). Subtotal: $", subtotal)

  elif labs == 2:
    print("Lavadora Whirlpool 17 Kg Blanca $7,990.00")
    nlavs = int(input("Ingresa el número de lavadoras deseadas: "))
    if nlavs >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nlavs * 7990
      total_final += subtotal
      print("Has seleccionado", nlavs, "lavadora(s). Subtotal: $", subtotal)

  elif labs == 3:
    print("Estufa Mabe EM7654BFIS2 Piso 30 Plata Mercury $9,169.00")
    nestufas = int(input("Ingresa el número de estufas deseadas: "))
    if nestufas >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nestufas * 9169
      total_final += subtotal
      print("Has seleccionado", nestufas, "estufa(s). Subtotal: $", subtotal)

  elif labs == 4:
    print("Licuadora Ninja Professional Blender 3 Velocidades Negra $1,890.00")
    nlic = int(input("Ingresa el número de licuadoras deseadas: "))
    if nlic >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nlic * 1890
      total_final += subtotal
      print("Has seleccionado", nlic, "licuadora(s). Subtotal: $", subtotal)

  elif labs == 5:
    print("Freidora de Aire Gourmia de 7.5 L / 8 Qt con 12 Preajustes $1,690.00")
    nfreid = int(input("Ingresa el número de freidoras deseadas: "))
    if nfreid >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nfreid * 1690
      total_final += subtotal
      print("Has seleccionado", nfreid, "freidora(s). Subtotal: $", subtotal)

  elif labs == 6:
    print("Horno de Microondas Whirlpool 1.1 Pies Cúbicos Silver $2,399.00")
    nhornos = int(input("Ingresa el número de hornos deseados: "))
    if nhornos >= 4:
      print("No existen tantos en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nhornos * 2399
      total_final += subtotal
      print("Has seleccionado", nhornos, "horno(s). Subtotal: $", subtotal)

  elif labs == 7:
    print("Batidora 2 en 1 Hamilton Beach Modelo 64650 $849.00")
    nbatid = int(input("Ingresa el número de batidoras deseadas: "))
    if nbatid >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nbatid * 849
      total_final += subtotal
      print("Has seleccionado", nbatid, "batidora(s). Subtotal: $", subtotal)

  elif labs == 8:
    print("Cafetera Oster para Espresso y Cappuccino Plata con Negro $1,607.60")
    ncaf = int(input("Ingresa el número de cafeteras deseadas: "))
    if ncaf >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = ncaf * 1607.60
      total_final += subtotal
      print("Has seleccionado", ncaf, "cafetera(s). Subtotal: $", subtotal)

  elif labs == 9:
    print("Wafflera Hamilton Beach Antiadherente Negro $599.00")
    nwaffle = int(input("Ingresa el número de waffleras deseadas: "))
    if nwaffle >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nwaffle * 599
      total_final += subtotal
      print("Has seleccionado", nwaffle, "wafflera(s). Subtotal: $", subtotal)

  elif labs == 10:
    print("Sandwichera Hamilton Beach Antiadherente Azul $899.00")
    nsndw = int(input("Ingresa el número de sandwicheras deseadas: "))
    if nsndw >= 4:
      print("No existen tantas en existencias.")
      print("Presione Enter para regresar al menú.")
      input()
    else:
      subtotal = nsndw * 899
      total_final += subtotal
      print("Has seleccionado", nsndw, "sandwichera(s). Subtotal: $", subtotal)

 
 
  
  
  
  
  
  else:
    print("Producto no válido. Por favor, selecciona una opción del 1 al 10.")
  
  
  sndlbs = input("¿Quieres comprar otro producto? (si/no): ")
  if sndlbs == "no":
    break


print("Gracias por tu compra. El total acumulado de tu compra es: $",total_final)



      



#else: 
 #   print ("Gracias por visitar HGMALL")
  # break





#lb= (int(input("Escribe el número del producto que desea comprar ")))

#while 
#if lb == 1:
 #clb= (int(input("Ingresa la cantidad de productos que quieras")))
 #if clb>=5:
  #print ("Demasiados productos intentelo de nuevo")
  #Regresar menu
 #else :
  # print


  