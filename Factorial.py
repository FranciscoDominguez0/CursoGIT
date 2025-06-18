# Pedimos al usuario un número entero
n = int(input("Ingresa un número entero para calcular su factorial: "))

# Validamos que no sea negativo
if n < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"El factorial de {n} es: {factorial}")
