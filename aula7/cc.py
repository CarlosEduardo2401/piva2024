valor_compra = float(input("Digite o valor da compra: R$ "))

# Calcula o desconto com base na tabela
if valor_compra <= 1000:
    desconto = valor_compra * 0.10  # 10% de desconto
elif valor_compra <= 5000:
    desconto = valor_compra * 0.20  # 20% de desconto
else:
    desconto = valor_compra * 0.30  # 30% de desconto

# Calcula o valor total com o desconto aplicado
valor_total = valor_compra - desconto

# Exibe o valor do desconto e o valor total da compra
print(f"Desconto aplicado: R$ {desconto:.2f}")
 print(f"Valor total da compra: R$ {valor_total:.2f}")