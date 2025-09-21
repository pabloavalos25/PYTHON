edad=int(input("ingrese su edad"))
if edad >=18:
    print("Usted es mayor de edad")
print()
#ejercicio_2
nota=float(input("ingrese su nota"))
if nota >= 6:
    print("Usted está aprobado")
else:
    print("Usted desaprobó")
#ejercicio_3
numero=int(input("ingrese un número par"))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("por favor, ingrese un número par")
#ejercicio_4
soli_edad=int(input("ingrese su edad"))

if soli_edad >1 and soli_edad<12:
    print("NIÑO")
elif soli_edad >=12 and soli_edad <18:
    print("ADOLESCENTE")
elif soli_edad >18 and soli_edad <30:
    print("ADULTO/A JOVEN")
elif soli_edad >30:
    print("ADULTO/A")
print()
#ejercicio_5
contraseña= input("ingrese una constraseña: ")

if 8 <= len(contraseña) <=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una constraseña entre 8 y 14 caracteres")
print()
#ejercicio_6    
from statistics import mean,median,mode
import random
numeros_aleatorios=[random.randint(1, 100) for i in range(50)]
mean=mean(numeros_aleatorios)
median=median(numeros_aleatorios)
mode=mode(numeros_aleatorios)

print("media: ", median)
print("mean", mean)
print("mode", mode)

if mean > median > mode:
    print("has sesgo positivo hacia la derecha")
elif mean < median < mode:
    print("hay sesgo negativo (hacia la izquierda)")
elif mean == median == mode:
    print("no hay sesgo")
else:
    print("no cumple con los criterios")
print()
#ejercicio_7
texto_letras=input("Ingrese una palabra:")

if texto_letras[-1].lower() in "aeiou":
    texto_letras=texto_letras+"!"

print(texto_letras)
print()
#ejercicio_8
nombre=input("Ingrese su nombre")
num= int(input("elija entre los números 1, 2 o 3")) 

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
print()
#ejercicio_9
terremoto=float(input("ingrese el valor de la magnitud sismo/terremoto (ej:7.0)"))

if terremoto < 3:
    print("Muy leve (imperceptible)")
elif terremoto >3 and terremoto < 4:
    print("Moderado (ligeramente perceptible)")
elif terremoto >=5 and terremoto <6:
    print("Fuerte, puede causar daños en estructuras débiles")
elif terremoto >=6 and terremoto <7:
    print("Muy fuerte, puede causar daños significativos")
elif terremoto >= 7:
    print("Extremo, puede causar daños graves a gran escala")
print()
#ejercicio_10
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

hemisferio = input("Ingrese el hemisferio en el que se encuentra (Norte/Sur): ")
mes = input("Ingrese el mes que desea saber (Ej: Enero, Febrero, etc): ")
dia = int(input("Ingrese el día que desea saber: "))

if hemisferio == "Norte":
    if (mes == "Septiembre" and dia >= 21) or (mes in ["Abril", "Mayo"]) or (mes == "Junio" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "Diciembre" and dia >= 21) or (mes in ["Julio", "Agosto"]) or (mes == "Marzo"):
        estacion = "Verano"
    elif (mes == "Septiembre" and dia >= 21) or (mes in ["Octubre", "Noviembre"]) or (mes == "Diciembre" and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"

elif hemisferio == "Sur":
    if (mes == "Septiembre" and dia >= 21) or (mes in ["Octubre", "Noviembre"]) or (mes == "Diciembre" and dia <= 20):
        estacion = "Primavera"
    elif (mes == "Diciembre" and dia >= 21) or (mes in ["Enero", "Febrero"]) or (mes == "Marzo" and dia <= 20):
        estacion = "Verano"
    elif (mes == "Marzo" and dia >= 21) or (mes in ["Abril", "Mayo"]) or (mes == "Junio" and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Invierno"
    
print("Estás en la estación:", estacion)