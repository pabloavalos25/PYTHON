def factorial(n):
    if n == 0 or n == 1:     # caso base
        return 1
    return n * factorial(n - 1)   # caso recursivo


def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"Factorial de {i} = {factorial(i)}")


# 2) Fibonacci recursivo

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(fibonacci(i), end=" ")
    print()



# 3) Potencia recursiva

def potencia(base, exponente):
    if exponente == 0:       # caso base
        return 1
    return base * potencia(base, exponente - 1)



# 4) Convertir decimal a binario (recursivo)

def decimal_a_binario(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_a_binario(n // 2) + str(n % 2)


# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:    # caso base
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])   # recursión sin extremos



# 6) Suma de dígitos recursiva

def suma_digitos(n):
    if n < 10:               # caso base
        return n
    return (n % 10) + suma_digitos(n // 10)



# 7) Pirámide de bloques

def contar_bloques(n):
    if n == 1:               # caso base
        return 1
    return n + contar_bloques(n - 1)



# 8) Contar ocurrencias de un dígito

def contar_digito(numero, digito):
    if numero == 0:          # caso base
        return 0
    ultimo = numero % 10
    suma = 1 if ultimo == digito else 0
    return suma + contar_digito(numero // 10, digito)