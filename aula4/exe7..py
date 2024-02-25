valor_deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))
taxa_juros_decimal = taxa_juros / 100
rendimento = valor_deposito * taxa_juros_decimal
valor_total = valor_deposito + rendimento
print(f"O valor do rendimento é: R${rendimento:.2f}")
print(f"O valor total após o rendimento é: R${valor_total:.2f}")
