precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melon': 3000, 'Uva': 1450 }

#Ejercicio_1

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print (precios_frutas)

#Ejercicio_2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800

#Ejercicio_3

frutas= list(precios_frutas.keys())
print(frutas)

#Ejercicio_4

contactos={}

for i in range(5):
    nombre_contacto=input(f"Ingrese el nombre del contacto {i + 1}: ")
    numero_contacto=int(input(f"Ingrese el número de teléfono de {nombre_contacto}:"))
    contactos[nombre_contacto] = numero_contacto

buscar_contacto=input("Ingrese el nombre del contacto que desee buscar: ")

if buscar_contacto in contactos:
    print(f"El numero de {buscar_contacto} es: {contactos[buscar_contacto]}")
else:
    print("No se encontro contacto con el nombre solicitado")

#Ejercicio_5

palabras_unicas={}
recuento={}

frase=input("Ingrese una frase: ")

palabras= frase.split()

palabras_unicas = set(palabras)
print("\nPalabras únicas: ")
print(palabras_unicas)

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] +=1
    else:
        recuento[palabra] =1

print("\nFrecuencia de cada palabra: ")
print(recuento)


#Ejercicio_6

alumnos= {}


for i in range(3):
    nombre_alumnos=input("Ingrese el nombre del alumno: ")
    
    nota=[] #Lista temporal    
    for j in range(3):
        notas=float(input(f"Ingrese las notas del alumno {nombre_alumnos}: "))
        nota.append(notas)

    promedio= sum(nota) / len(nota)
    alumnos[nombre_alumnos] = (tuple(nota), promedio)

print("\n Promedio de alumnos:")
for nombre_alumnos in alumnos:
    print(f"{nombre_alumnos}: {alumnos[nombre_alumnos][1]:.2f}")

#Ejercicio_7

parcial_uno=[]
parcial_dos=[]

alumnos=int(input("Ingrese la cantidad de alumnos: "))

for i in range(alumnos):
    nombre=input(f"\n Ingrese el nombre del alumno {i + 1}:")

    nota_uno = float(input("Ingrese la nota del parcial 1:"))
    nota_dos = float(input("Ingrese la nota del parcial 2:"))

    if nota_uno >=6: #Aprobó el parcial uno
        parcial_uno.append(nombre)
    
    if nota_dos >=6: #Aprobó el parcial dos
        parcial_dos.append(nombre)

set1 = set(parcial_uno)
set2 = set(parcial_dos)

print("Alumnos que aprobaron ambos parciales:")
print(set1 & set2)

print("Alumnos que aprobaron solo uno de los dos parciales: ")
print(set1 ^ set2)

print("Alumnos que aprobaron al menos un parcial: ")
print(set1 | set2 )

#Ejercicio_8

producto={}

cantidad_productos=int(input("Cuantos productos desea agregar?"))

for i in range(cantidad_productos):
    los_productos=input(f"Ingrese el producto {i + 1}: ")
    stock=int(input(f"Cual es el stock de {los_productos}: "))

    producto[los_productos]=(stock)

while True:
    print("---MENU DEL STOCK---")
    print("1. Consultar stock de productos")
    print("2. Agregar unidades a un producto")
    print("3. Agregar producto nuevo")
    print("4. Ver todos los productos")
    print("5. Salir")

    opcion=input("Seleccione la opción que desee: ")

    if not opcion.isdigit():
        print("Error, debe selecciona una opción correcta")
        continue
    opcion=int(opcion)

    match opcion:
        case 1:
            nombre=input("Ingrese el nombre del producto a consultar: ")

            if nombre in producto:
                print(f"El stock de: {nombre} es de: {producto[nombre]}")
            else:
                print("No existe el producto consultado en el inventario")
        case 2:
            nombre=input("Ingrese el nombre del producto: ")
            if nombre in producto:
                agregar=int(input("Cuantas unidades desea agregar? "))
                producto[nombre] += agregar
                print(f"Stock actualizado de {nombre}: {producto[nombre]}")
            else:
                print("El producto consultado no existe en el inventario")
        case 3:
            nombre=input("Ingrese el nombre del producto: ")
            stock=int(input(f"Ingrese el stock de {nombre}"))
            producto[nombre]= stock
            
            print(f"Producto {nombre} con stock {stock} agregado con éxito!")
        case 4:
            print("Inventario completo:")
            for nombre, stock in producto.items():
                print(f"{nombre}: {stock}")
        case 5:
            print("Programa finalizado, saludos")
            break
        case _:
            print("ERROR")

#Ejercicio_9

agenda = {}

cantidad_eventos=int(input("Ingrese la cantidad de eventos a cargar: "))

for i in range(cantidad_eventos):
    dia=input(f"Ingrese el día del evento {i+1}: ")
    hora=input(f"Ingrese la hora del evento {i + 1}: ")
    evento=input("Ingrese el nombre del evento a guardar: ")

    clave = (dia, hora)
    agenda[clave] = evento

while True:
    print("---Agenda de eventos---")
    print("1. Consultar eventos")
    print("2. Agregar nuevo evento")
    print("3. Ver todos los eventos cargados")
    print("4. Salir")

    eleccion= input("Seleccione la opción que desee consultar: ")

    if not eleccion.isdigit():
        print("Error, debe seleccionar una opción correcta")
        continue
    eleccion=int(eleccion)

    match eleccion:
        case 1:
            dia= input("Ingrese el día: ")
            hora= input("Ingrese la hora (ejemplo 14:00): ")
            clave= (dia, hora)

            if clave in agenda:
                print(f"el {dia} a las {hora} hay {agenda[clave]}")
            else:
                print("No hay eventos disponibles para esa fecha")
        case 2:
            dia=input("Ingrese el día: ")
            hora=input("Ingrese la hora: ")
            evento=input("Ingrese el nombre del nuevo evento: ")

            clave = (dia, hora)

            agenda[clave] = evento
            print("Evento cargado exitosamente! ")
        case 3:
            print("Agenda completa:")

            for (dia, hora), evento in agenda.items():
                print(f"{dia} - {hora}: {evento}")

        case 4:
            print("Saliendo del sistema, saludos!")
            break
        case _:
            print("Error")

#Ejercicio_10

original= {}
invertido = {}

cantidad_paises=int(input("Cuantos paises desea ingresar?"))

for i in range(cantidad_paises):
    pais=input(f"Ingrese el nombre del país {i + 1}: ")
    capital=input(f"Ingrese la capital del {pais}: ")

    original[pais] = capital
    invertido [capital] = pais

print("Diccionario original (País - Capital):")
print(original)

print("Diccionario invertido (Capital - País):")
print(invertido)


