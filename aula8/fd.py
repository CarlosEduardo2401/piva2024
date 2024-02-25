# Função para somar dois números
def somar(a, b):
    return a + b

# Função para dividir dois números
def dividir(a, b):
    if b == 0:
        return "Não é possível dividir por zero."
    else:
        return a / b

# Solicitar entrada do usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar a soma e a divisão
soma = somar(num1, num2)
divisao = dividir(num1, num2)

# Exibir os resultados
print(f"A soma de {num1} e {num2} é: {soma}")
print(f"A divisão de {num1} por {num2} é: {divisao}")
