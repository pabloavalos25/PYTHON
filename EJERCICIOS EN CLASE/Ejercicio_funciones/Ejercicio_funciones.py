import random

scuderias=["Ferrari","Mclaren","Mercedes","Williams","RedBull","Sauber","Haas",]

aleatorio = random.choice(scuderias)

#Se le pide al usuario que agregue las letras
Letra= input("Ingrese la letra: ")

def mostrar_palabra(palabra , letra_adivinada):
    return " ".join([Letra if Letra in letra_adivinada else "_" for letra in palabra])