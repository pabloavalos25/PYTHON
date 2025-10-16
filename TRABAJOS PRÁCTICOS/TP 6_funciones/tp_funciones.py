#Ejercicio_1
def imprimir_hola_mundo():
        print(f"Hola mundo")

imprimir_hola_mundo()

#Ejercicio_2
def saludar_usuario():
        saludo=input("Como es su nombre? ")
        print(f"Hola, {saludo}!")

saludar_usuario() 

#Ejercicio_3

def informacion_personal():
        nombre=input("Cual es su nombre?: ")
        apellido=input("Cual es su apellido?: ")
        edad=input("Cual es su edad?: ")
        residencia=input("Cual es su residencia?: ")

        print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal()
#Ejercicio_4

def calcular_area_circulo(radio):
        pi = 3.1416
        area = pi * (radio ** 2)
        return area
def calcular_perimetro(radio):
        pi = 3.1416
        perimetro = 2 * pi * radio
        return perimetro

radio = float(input("Ingrese el radio del circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro(radio)

print(f"El area del circulo es: {area:.2f}")
print(f"El perimetro del circulo es: {perimetro:.2f}")

#Ejercicio_5

def segundos_a_horas(segundos):
        seg_a_hora= (segundos / 3600)

        print(f"la hora es: {seg_a_hora:.2f}")
segundos=float(input("Ingrese la cantidad de segundos a convertir en horas: "))
segundos_a_horas(segundos)

#Ejercicio_6

def tabla_multiplicar(numero):
        for i in range(11):
                multiplicar= numero * i
                print(f"{numero} x {i} = {multiplicar}")

numero=int(input("Ingrese el número a multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio_7

def operaciones_basicas(a,b):
        suma = a + b
        resta = a - b
        multiplicacion= a * b

        if b != 0:
                division = a / b
        else:
                division = "No se puede dividir por cero"
        return (suma, resta, multiplicacion, division)

a= float(input("Ingrese el primer numero: "))
b= float(input("Ingese el segundo numero: "))

resultado = operaciones_basicas(a,b)

print(f"Suma: {resultado[0]}")
print(f"resta: {resultado[1]}")
print(f"multiplicacion: {resultado[2]}")
print(f"Division: {resultado[3]}")

#Ejercicio_8

def calcular_imc(peso, altura):
        imc = peso / (altura ** 2)
        return imc

peso = float(input("Ingrese el peso en kg: "))
altura = float(input("Ingrese la la altua en metros: "))

imc = calcular_imc(peso, altura)

print(f"su IMC es de: {imc:.2f}")

#Ejercicio_9

def celsius_a_fahrenheit(celcius):
        conversion = (celcius * 9 / 5) + 32
        print(f"la conversión de {celcius} es: {conversion:.2}")

celcius = float(input("Ingrese los grados celcius que desee convertir: "))
celsius_a_fahrenheit(celcius)

#Ejercio_10

def calcular_promedio(a,b,c):
        promedio= (a + b + c) / 3
        print(f"el promedio de las 3 notas es {promedio:.2f}")

a=float(input("Ingrese la primer nota: "))
b=float(input("Ingrese la segunda nota: "))
c=float(input("Ingrse la tercer nota: "))

calcular_promedio(a,b,c)