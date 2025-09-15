intro= print("MENÚ LIBROS")

lista_libros= []
cant_ejemplares= []


inicio=1
while inicio >0:
    menu=int(input("1. ingrese la lista de títulos \n2. ingrese la lista de ejemplares \n3. mostrar catálogo \n4. consultar titulo \n5. Ejemplares agotados \n6. agregar título \n7. actualizar ejemplares \n8. Ver catálogo \n9. salir del programa \n"))

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
        consulta=input("que título desea consultar? ")
        for cont  in range(len(lista_libros)):
            if lista_libros[cont]==consulta:
                print(f"el libro:{lista_libros[cont]} tiene disponibles: {cant_ejemplares[cont]}")
    elif menu == 5:
        for cont in range (len(lista_libros)):
            if cant_ejemplares[cont]==0:
                print(f"el titulo es: {lista_libros[cont]}")
    elif menu == 6:
        titulo=input("que título desea agregar?")
        lista_libros.append(titulo)
        cantidad=int(input("ingrese la cantidad de ejemplares del nuevo libro"))
        cant_ejemplares.append(cantidad)

    elif menu == 7:
        #devolucion
        opcion=str(input("\n Que deseas hacer?\nA. Prestar un libro \nB. Devolver un libro \nC. Salir"))

        if opcion == "A":
            libro_prestar=input("Ingrese el libro que desea prestar: ")
            if libro_prestar in lista_libros:
                if lista_libros (len(libro_prestar)) > 0:
                    lista_libros[cont] -= 1
                    print(f"Se ha prestado el ejemplar de: {libro_prestar}.")
                else:
                    print(f"No quedan mas ejemplares de: {libro_prestar}.")
            else:
                print("El libro no existe en la biblioteca!")


        elif opcion == "B":
            devolucion=input("Ingrese el libro que desea devolver: ")
            if devolucion in lista_libros:
                lista_libros[devolucion] += 1
                print(f"Se devolvió el ejemplar de: {devolucion}")
            else:
                print("El ejemplar mencionado no existe en la biblioteca")


        elif opcion == "C":
            print("Saliendo del sistema....")
            break
    elif menu == 8:
        for cont in range (len(lista_libros)):
            print(f"titulo: {lista_libros[cont]} cantidad: {cant_ejemplares[cont]}")
    else:
        break
