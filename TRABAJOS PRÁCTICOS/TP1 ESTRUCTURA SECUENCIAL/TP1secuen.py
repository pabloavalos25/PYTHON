#ejercicio_1
print ("Hola Mundo!")
print()
#ejercicio_2
nombre = input("ingrese su nombre")
print (f"hola, {nombre}!")
print()
#ejercicio_3 
nom= input("Ingrese su nombre") 
ape= input("ingrese su apellido")
edad= input("ingrese su edad")
pais= input("ingrese país de residencia")

print (f"soy {nom} {ape}, tengo {edad} años y vivo en {pais}")
print()
#ejercicio_4
import math

radio=float(input("Ingrese el radio del circulo"))

area= math.pi*radio**2
Perimetro=2*math.pi*radio

print(f"El área del circulo es: {area:.2f}")
print(f"EL perimetro del circulo es: {Perimetro:.2f}")
print()
#ejercicio_5
segundos=int(input("Ingrese la cantidad de segundos que desea convertir"))
print (segundos)

horas= segundos/3600
print (f"{segundos} equivale a {horas:.2f} horas")
print()
#ejercicio_6
numero_uno= int(input("agrega un número"))
print (f"tabla de multiplicar del número {numero_uno}")
for i in range (1,11):
    print (f"{numero_uno} x {i} = {numero_uno*i}")
print()
#ejercicio_7

numero1=int(input("ingrese un número entero"))
numero2=int(input("ingrese el segundo número entero"))

numero1>0
numero2>0

suma=numero1+numero2
print(suma)

resta=numero1-numero2
print(resta)

multiplicacion=numero1*numero2
print(multiplicacion)

division=numero1/numero2
print(division)
print()
#ejercicio_8

def calcular_imc(peso,altura):
    return (peso/altura**2)
altura=float(input("introduzca su altura"))
peso= float(input("introduzca su peso"))

imc= calcular_imc(peso,altura)
print (f"su incide de masa corporal es de: {imc:.2f}")
print()
#ejercicio_9

grados_celcius=float(input("Ingrese los grados celcius"))
fahrenheit= grados_celcius * 9/5 + 32
print(f"{grados_celcius}°C son: {fahrenheit:.2f}°F")
print()
#ejercicio_10

num1=float(input("ingrese el primer número"))
num2=float(input("ingrese el segundo número"))
num3=float(input("ingrese el tercer número"))

promedio= (num1+num2+num3) / 3
print(f"el promedio de los tres números es: {promedio:.2f}")