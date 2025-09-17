#Ejercicio_1
for i in range (0,101):
 print(i)

#Ejercicio_2
numero_user=int(input("Ingrese un número entero: "))
digitos_num= len(str(numero_user))
print(f"el número {numero_user} tiene {digitos_num} dígito/s.")

#Ejercicio_3
valor_1=int(input("ingrese el primer valor a sumar: "))
valor_2=int(input("ingrese el segundo valor: "))

suma = 0
for i in range (valor_1 + 1, valor_2):
    suma += i
print(f"la suma de de los números entre {valor_1} y {valor_2} excluyendolos es {suma}")

#Ejercicio_4

suma = 0
while True:
    num_1=int(input("ingrese el número entero a sumar: "))
    if num_1 == 0:
       break
    suma += num_1
print(f"la suma total es de: {suma}")

#Ejercicio_5
import random

num_random= random.randint(0,9)

intentos = 0
acierto= False 

while not acierto:
   num_user= int(input("adivina el número entre 0 y 9: "))
   intentos += 1

   if num_user == num_random:
        acierto = True
   else:
      print("No es el número correcto, intenta nuevamente ")

print(f"Excelente, el número era {num_random}, te tomó {intentos} intentos lograrlo")


#Ejercicio_6

for i in range (100, -1 , -2):
   print (i)

#Ejercicio_7
suma = 0 
num_positivo=int(input("ingrese un número positivo: "))
for i in range (0, num_positivo + 1 ):
    suma += 1
print(f"la suma entre todos los número entre 0 y {num_positivo} es {suma}")

#Ejercicio_8

N = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range (N):
   num=int(input(f"ingrese el núnmero {i+1}: "))
   
   if num % 2 ==0:
      pares += 1
else:
   impares += 1


   if num > 0:
      positivos += 1

   elif num < 0:
      negativos +=1

print (f"Resultados\nNumero Pares {pares}\nNumeros impares{impares}\nNumeros positivos {positivos}\nNumeros negativos{negativos} ")

#Ejercicio_9

N=100

suma=0

for i in range (N):
   numero= int(input(f"ingrese el número {i+1}"))
   suma += numero

media = suma / N

print(f"Resultados:\nLa media de los {N} numeros ingresados es: {media}")

#Ejercicio_10

Num_usuario=int(input("ingrese un número entero: "))
invertido = 0
while num > 0:
   digito=Num_usuario % 10
   invertido = invertido * 10 + digito
   Num_usuario //= 10

print(f"El Número invertido es: {invertido} ")