
salario_atual = float(input("Digite o salário atual do funcionário: "))

percentual_aumento = float(input("Digite o percentual de aumento: "))
valor_aumento = salario_atual * (percentual_aumento / 100)


novo_salario = salario_atual + valor_aumento
print(f"O valor do aumento é: R${valor_aumento:.2f}")
print(f"O novo salário, após o aumento, é: R${novo_salario:.2f}")
