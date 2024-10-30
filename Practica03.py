print("Sistemapara calcular el promedio de un alumno")
# Creamos una variable para el nombre
nombre = input ("Para comnezar, Cual es tu nombre?: ")
# Creamos variables para las materias 
matematicas = int(input(nombre + " Cual es tu calificacion de matematicas?: "))
quimica = int(input( nombre+ " Cual es tu calificacion de quimica?: "))
español = int(input(nombre + " Cual es tu calificacion de español?: "))
Yo_y_los_demas = int(input(nombre + " Cual es tu calificacion de Yo y los demas?: "))
plc = int(input(nombre + " Cual es tu calificacion de PLC?: "))
Ingles = int(input(nombre + " Cual es tu calificacion de Ingles?: "))
Historia = int(input(nombre + " Cual es tu calificacion de Historia?: "))
promedio = (matematicas + quimica + español + Yo_y_los_demas + plc + Ingles + Historia) / 7

if promedio >= 10:
 print("Haz hecho un trabajo excelente "+ nombre+" aprobaste con: ", promedio)

elif promedio >= 8:
  print("Buen trabajo tu promedio fue de: ", promedio)
elif promedio == 7:
  print("Apenas lo lograste tu promedio fue de ", promedio)
else:
  print("No lo lograste tu promedio fue de:", promedio)


