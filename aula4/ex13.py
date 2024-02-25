# Solicita ao usuário que insira o valor do salário mínimo
salario_minimo = float(input("Digite o valor do salário mínimo: "))

# Solicita ao usuário que insira a quantidade de quilowatts consumida
quilowatts_consumidos = float(input("Digite a quantidade de quilowatts consumida: "))

# Calcula o valor de cada quilowatt (um oitavo do salário mínimo)
valor_por_quilowatt = salario_minimo / 8

# Calcula o valor a ser pago pela residência
valor_total = valor_por_quilowatt * quilowatts_consumidos

# Calcula o valor com desconto de 15%
desconto = 0.15
valor_com_desconto = valor_total * (1 - desconto)

# Exibe os resultados
print(f"O valor de cada quilowatt é: R${valor_por_quilowatt:.2f}")
print(f"O valor a ser pago pela residência é: R${valor_total:.2f}")
print(f"O valor a ser pago com desconto de 15% é: R${valor_com_desconto:.2f}")
