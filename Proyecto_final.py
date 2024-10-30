

# Ponemos valores a las constantes que vamos ocupar durante el programa
ft = 99
gk = 259
print("HOLA BIENVENIDOS A DINOSAUR KINGDOM")
print("Los horarios del parque son de 11:00 a 21:00 De Lunes a Domingo")
print("Presione Enter para continuar..")
input()
print("FORMAS DE ACCESAR")
print("1. Entrada general")
print("2. Paquetes")
# Creamos una variable para la entrada
entrada= int(input("Presione 1 si desea una Entrada General, 2 si desea un Paquete   "))

if entrada == 1:
  print("ENTRADA GENERAL")
  print ("Entrada general......................... $799")
  eg = 799
  print ("Presione enter para continuar")
  input()
  print ("EXPERIENCIAS EXTRAS: RECUERDOS JURÁSICOS ")
  print ("1. Servicio de fotos alrededor del parque........ $99")
  print ("2. GO KARTS.......................................$259")
  print ("Desea comprar una experiencia extra?  ")

  decision = int(input("1 (Si) 2 (No) "))
# Creamos una variable para cada decision ya sea 1 o 2 
  if decision == 1:

   print ("1. Servicio de fotos alrededor del parque........ $99")
   print ("2. GO KARTS.......................................$259")
   dex = int(input("Elija una experiencia extra escribiendo el numero "))

   if dex == 1:
    print ("Ha elegido Servicio de Fotos $99")
    print ("Desea comprar otra experiencia extra?  ")
    decision1  = int(input("1 (Si) 2 (No) "))

    if decision1 == 1:

     
     print ("2. GO KARTS.......................................$259")
     dex1 = int(input("Elija una experiencia extra escribiendo el numero "))

     if dex1 == 2 :
      print ("Presione enter para seguir con el pago")
      total = eg + ft + gk
      print ("DINOSAUR KINGDOM")
      print ("Entrada general.................................. $799")
      print ("EXPERIENCIAS EXTRAS")
      print ("1. Servicio de fotos alrededor del parque........ $99")
      print ("2. GO KARTS.......................................$259")
      print ("Su total a pagar es de $", total)
      print ("Disfrute su visita!!!!")

  

    else:
     total = eg + ft
     print ("DINOSAUR KINGDOM")
     print ("Entrada general.................................. $799")
     print ("EXPERIENCIAS EXTRAS")
     print ("1. Servicio de fotos alrededor del parque........ $99")
     print ("Su total a pagar es de $", total)
     print ("Disfrute su visita!!!!")

   if dex == 2:
    print ("Ha elegido Go Karts $259")
    print ("Desea comprar otra experiencia extra?  ")
    decision1  = int(input("1 (Si) 2 (No) "))

    if decision1 == 1:

     
     print ("1. Sevicio de fotos.......................................$99")
     dex1 = int(input("Elija una experiencia extra escribiendo el numero "))

     if dex1 == 1 :
      print ("Presione enter para seguir con el pago")
      total = eg + ft + gk
      print ("DINOSAUR KINGDOM")
      print ("Entrada general.................................. $799")
      print ("EXPERIENCIAS EXTRAS")
      print ("1. Servicio de fotos alrededor del parque........ $99")
      print ("2. GO KARTS.......................................$259")
      print ("Su total a pagar es de $", total)
      print ("Disfrute su visita!!!!")
    
    else:
     total = eg + gk
     print ("DINOSAUR KINGDOM")
     print ("Entrada general.................................. $799")
     print ("EXPERIENCIAS EXTRAS")
     print ("2. Go Karts.......................................$259")
     print ("Su total a pagar es de $", total)
     print ("Disfrute su visita!!!!")

  else : 
    print ("DINOSAUR KINGDOM")
    print ("Entrada general.................................. $799")
    print ("Su total a pagar es de $", eg)
    print ("Disfrute su visita!!!!")
     


    
    


 
  


             
if entrada == 2:
 



 print ("Estos son nuestros paquetes (todos ya incluyen la entrada al parque. Solo puede comprar un paquete por entrada)")
 print ("1. Atracciones Acuaticas......................... $1199")
 print ("2. Velociraptor Pass..............................$1149")
 
 
# Creamos variables a utilizar cuando son Paquetes
 aa = 1199
 vp = 1149
 
 # Hacemos lo mismo que en el caso de la entrada

 paquete= int(input("Seleccione el numero del paquete que desea: "  ))
 
 if paquete == 1:
  print ("Has seleccionado el paquete *Atracciones Acuaticas* con un costo de $1199")
  print ("Presione enter para continuar")
  input()
  print ("EXPERIENCIAS EXTRAS: RECUERDOS JURÁSICOS ")
  print ("1. Servicio de fotos alrededor del parque........ $99")
  print ("2. GO KARTS.......................................$259")
  
  print ("Desea comprar una experiencia extra?  ")
  dp1 = int(input("1(Si) 2 (No) :"))

  if dp1 == 1:

   print ("1. Servicio de fotos alrededor del parque........ $99")
   print ("2. GO KARTS.......................................$259")
   dex = int(input("Elija una experiencia extra escribiendo el numero "))

   if dex == 1:
    print ("Ha elegido Servicio de Fotos $99")
    print ("Desea comprar otra experiencia extra?  ")
    decision1  = int(input("1 (Si) 2 (No) "))

    if decision1 == 1:

     
     print ("2. GO KARTS.......................................$259")
     dex1 = int(input("Elija una experiencia extra escribiendo el numero "))

     if dex1 == 2 :
      print ("Presione enter para seguir con el pago")
      total = aa + ft + gk
      print ("DINOSAUR KINGDOM")
      print ("Atracciones Acuaticas............................ $1199")
      print ("EXPERIENCIAS EXTRAS")
      print ("1. Servicio de fotos alrededor del parque........ $99")
      print ("2. GO KARTS.......................................$259")
      print ("Su total a pagar es de $", total)
      print ("Disfrute su visita!!!!")

  

    else:
     total = aa + ft
     print ("DINOSAUR KINGDOM")
     print ("Atracciones Aacuaticas........................... $1199")
     print ("EXPERIENCIAS EXTRAS")
     print ("1. Servicio de fotos alrededor del parque........ $99")
     print ("Su total a pagar es de $", total)
     print ("Disfrute su visita!!!!")

   if dex == 2:
    print ("Ha elegido Go Karts $259")
    print ("Desea comprar otra experiencia extra?  ")
    decision1  = int(input("1 (Si) 2 (No) "))

    if decision1 == 1:

     
     print ("1. Sevicio de fotos.......................................$99")
     dex1 = int(input("Elija una experiencia extra escribiendo el numero "))

     if dex1 == 1 :
      print ("Presione enter para seguir con el pago")
      total = aa + ft + gk
      print ("DINOSAUR KINGDOM")
      print ("Atracciones Acuaticas............................ $1199")
      print ("EXPERIENCIAS EXTRAS")
      print ("1. Servicio de fotos alrededor del parque........ $99")
      print ("2. GO KARTS.......................................$259")
      print ("Su total a pagar es de $", total)
      print ("Disfrute su visita!!!!")
    
    else:
     total = aa + gk
     print ("DINOSAUR KINGDOM")
     print ("Atracciones Acuáticas.................................. $1199")
     print ("EXPERIENCIAS EXTRAS")
     print ("2. Go Karts.......................................$259")
     print ("Su total a pagar es de $", total)
     print ("Disfrute su visita!!!!")

  else : 
    print ("DINOSAUR KINGDOM")
    print ("Atracciones Acuaticas.................................. $1199")
    print ("Su total a pagar es de $", aa)
    print ("Disfrute su visita!!!!")
     

 else: 
  print ("Has seleccionado el paquete *Velociraptor Pass* con un costo de $1149")
  print ("Presione enter para continuar")
  input()
  print ("EXPERIENCIAS EXTRAS: RECUERDOS JURÁSICOS ")
  print ("1. Servicio de fotos alrededor del parque........ $99")
  print ("2. GO KARTS.......................................$259")
  
  print ("Desea comprar una experiencia extra?  ")
  dp1 = int(input("1(Si) 2 (No) :"))

  if dp1 == 1:

   print ("1. Servicio de fotos alrededor del parque........ $99")
   print ("2. GO KARTS.......................................$259")
   dex = int(input("Elija una experiencia extra escribiendo el numero "))

   if dex == 1:
    print ("Ha elegido Servicio de Fotos $99")
    print ("Desea comprar otra experiencia extra?  ")
    decision1  = int(input("1 (Si) 2 (No) "))

    if decision1 == 1:

     
     print ("2. GO KARTS.......................................$259")
     dex1 = int(input("Elija una experiencia extra escribiendo el numero "))

     if dex1 == 2 :
      print ("Presione enter para seguir con el pago")
      total = vp + ft + gk
      print ("DINOSAUR KINGDOM")
      print ("Velociraptor Pass.................................$1499")
      print ("EXPERIENCIAS EXTRAS")
      print ("1. Servicio de fotos alrededor del parque........ $99")
      print ("2. GO KARTS.......................................$259")
      print ("Su total a pagar es de $", total)
      print ("Disfrute su visita!!!!")

  

    else:
     total = vp + ft
     print ("DINOSAUR KINGDOM")
     print ("Velociraptor Pass................................ $1149")
     print ("EXPERIENCIAS EXTRAS")
     print ("1. Servicio de fotos alrededor del parque........ $99")
     print ("Su total a pagar es de $", total)
     print ("Disfrute su visita!!!!")

   if dex == 2:
    print ("Ha elegido Go Karts $259")
    print ("Desea comprar otra experiencia extra?  ")
    decision1  = int(input("1 (Si) 2 (No) "))

    if decision1 == 1:

     
     print ("1. Sevicio de fotos.......................................$99")
     dex1 = int(input("Elija una experiencia extra escribiendo el numero "))

     if dex1 == 1 :
      print ("Presione enter para seguir con el pago")
      total = vp + ft + gk
      print ("DINOSAUR KINGDOM")
      print ("Velociraptor Pass.................................$1149")
      print ("EXPERIENCIAS EXTRAS")
      print ("1. Servicio de fotos alrededor del parque........ $99")
      print ("2. GO KARTS.......................................$259")
      print ("Su total a pagar es de $", total)
      print ("Disfrute su visita!!!!")
    
    else:
     total = vp + gk
     print ("DINOSAUR KINGDOM")
     print ("Velociraptor Pass.................................. $1149")
     print ("EXPERIENCIAS EXTRAS")
     print ("2. Go Karts.............................................$259")
     print ("Su total a pagar es de $", total)
     print ("Disfrute su visita!!!!")

  else : 
    print ("DINOSAUR KINGDOM")
    print ("Velociraptor Pass.................................. $1149")
    print ("EXPERIENCIAS EXTRAS")
    print ("Su total a pagar es de $", vp)
    print ("Disfrute su visita!!!!")







