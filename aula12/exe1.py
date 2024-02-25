# Solicitar ao usuário para digitar um número
numero = int(input("Digite um número: "))

# Mostrar o número digitado
print(f"Número digitado: {numero}")

# Verificar se o número é par ou ímpar
if numero % 2 == 0:
    print(f"{numero} é um número par.")
else:
    print(f"{numero} é um número ímpar.")

# Verificar se o número é maior que 30
if numero > 30:
    # Imprimir em ordem decrescente de 5 em 5 até zero
    for i in range(numero, -1, -5):
        print(i)
else:
    print("Digite outro número, pois é menor ou igual a 30.")
