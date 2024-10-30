#IMC
print("HOLA")
print("CONOCE TU INDICE DE MASA CORPORAL(IMC)")
print("PRESIONE ENTER PARA CONTINUAR")
input()
print("El indice de masa corporal es el resultado del cociente del peso y la estatutra")
print ("Si eres mayor de 20 anos se te dira tambien tu rango de peso (BAJO PESO, NORMAL, SOBREPESO, OBESIDAD)")
print("PRESIONE ENTER PARA CONTINUAR")
input()
#DECLARAMOS LAS VARIABLES QUE VAMOS A OCUPAR
peso= float(input("Ingrese su peso en kg:  "))
estatura= float(input("Ingresa su estatura en metros: ")) 
edad= int(input("Ingrese su edad: "))

imc = peso/estatura

if edad>=20:
    if imc<18.5: 
        print ("Tu IMC es de:" ,imc)
        print ("En base a tu edad: tienes BAJO PESO (Esto en base a un estandar entre la poblacion ADULTA)")
        print ("Gracias por particiapar")
#OCUPAMOS "AND" PARA QUE SI DOS CONDICIONES SE CUMPLEN ESTE IMPRIMA EL REUSLTADO
    if imc>=18.5 and imc<=24.9:
        print ("Tu IMC es de:" ,imc)
        print ("En base a tu edad: tienes PESO NORMAL (Esto en base a un estandar entre la poblacion ADULTA)")
        print ("Gracias por particiapar")

    if imc>=25 and imc<= 29.9:
        print ("Tu IMC es de:" ,imc)
        print ("En base a tu edad: tienes SOBREPESO (Esto en base a un estandar entre la poblacion ADULTA)")
        print ("Gracias por particiapar")

    if imc>=30:
        print ("Tu IMC es de:" ,imc)
        print ("En base a tu edad: tienes OBESIDAD (Esto en base a un estandar entre la poblacion ADULTA)")
        print ("Gracias por particiapar")

else:

    print ("Tu IMC es de:" ,imc)
    print ("Gracias por particiapar")





              

