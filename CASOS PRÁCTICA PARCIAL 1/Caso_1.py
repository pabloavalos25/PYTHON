intro= print("MENÚ LIBROS")

lista_libros= []
cant_ejemplares= []


inicio=1
while inicio <0:
    input("ingrese un valor del 1 al 8")
menu=int(input("1. ingrese la lista de títulos \n2. ingrese la lista de ejemplares \n3. mostrar catálogo \n4. consultar titulo \n5. Ejemplares agotados \n6. agregar título \n7. actualizar ejemplares \n8. salir del programa\n"))

if menu == 1:
    resp=int(input("cuantos títulos quiere ingresar? "))
    for cont in range (resp):
        libro=input("ingrese el libro: ")
        lista_libros.append(libro)
elif menu == 2:
    for cont in range(len(lista_libros)):
        ejemplares=int(input("ingrese la cantidad de ejemplares: "))
        cant_ejemplares.append(ejemplares)
        
elif menu == 3:
    for cont in range(len(lista_libros)):
        print(f"El ejemplar es:{lista_libros[cont]}la cantidad de copias es: {cant_ejemplares[cont]}")

elif menu == 4:
    consulta=("que título desea consultar? ")
    for consulta in range(lista_libros):
        print("copias disponibles: ", cant_ejemplares)
        if cant_ejemplares < 0:
            print("No hay ejemplares dispobiles")
elif menu == 5:
 
elif menu == 6:
    titulo=input("que título desea agregar?")
    lista_libros.append(titulo)
    cantidad=int(input("ingrese la cantidad de ejemplares del nuevo libro"))
    cant_ejemplares.append(cantidad)

elif menu == 7: