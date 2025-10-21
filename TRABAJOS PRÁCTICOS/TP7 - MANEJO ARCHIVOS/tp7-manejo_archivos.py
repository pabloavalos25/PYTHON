#Ejericio_1

productos= [
    "Arroz,1200,15",
    "Aceite,1500,10",
    "Fideos,980,25"
]
#Creo el archivo en modo escritura
with open("productos.txt","w", encoding="utf-8") as archivo:
    for producto in productos:
        archivo.write(producto + "\n")

#Ejercicio_2

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        #Quitar espacios y saltos de linea
        linea = linea.strip()
        #Separar los datos por coma
        nombre, precio, cantidad = linea.split(",")

        print(f"Proucto: {nombre}, precio: ${precio}, cantidad: {cantidad}")

#Ejericio_3

agregar_producto=input("Ingrese el producto nuevo: ")
precio_nuevo=float(input(f"Cual es el precio de {agregar_producto}: "))
cantidad_nueva=int(input(f"Cual es el stock de {agregar_producto}"))
        
with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{agregar_producto},{precio_nuevo},{cantidad_nueva}\n")

print("Producto agregado correctamente.") 

#Ejercicio_4

with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea= linea.strip()
        nombre,precio,cantidad=linea.split(",")
        producto={
            "Nombre": nombre,
            "Precio": float(precio), 
            "Cantidad": int(cantidad)
        }
        productos.append(producto) #Agregar diccionario a la lista

for p in productos:
    print(p)

#Ejercicio_5

with open("productos.txt", "r", encoding="utf-8") as archivo:

    buscar_producto=input("Ingrese el producto que ibas a buscar: ")
    encontrado=False
    
    for linea in archivo:
        nombre, precio, cantidad=linea.strip().split(",")
        if nombre.lower()== buscar_producto:
            print(f"producto: {nombre}, precio: {precio},cantidad: {cantidad}")
            encontrado=True
            break

if not encontrado:
    raise ValueError("Error, producto no encontrado.")

#Ejercicio_6

with open("productos.txt", "w", encoding="utf-8") as archivo:
    for producto in productos:
        archivo.write(",".join(producto) + "\n")
print("Archivo actualizado correctamente.")
