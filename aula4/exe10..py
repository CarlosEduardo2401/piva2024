import math


numero = float(input("Digite um número positivo e maior que zero: "))


if numero <= 0:
    print("Por favor, insira um número positivo e maior que zero.")
else:

    numero_quadrado = numero ** 2
    numero_cubo = numero ** 3
    raiz_quadrada = math.sqrt(numero)

    print(f"O número ao quadrado é: {numero_quadrado}")
    print(f"O número ao cubo é: {numero_cubo}")
    print(f"A raiz quadrada do número é: {raiz_quadrada:.4f}")
