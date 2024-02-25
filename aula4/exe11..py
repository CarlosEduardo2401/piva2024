# Solicita ao usuário que insira uma medida em pés
medida_em_pes = float(input("Digite a medida em pés: "))

# Realiza as conversões
polegadas = medida_em_pes * 12
jardas = medida_em_pes / 3
milhas = jardas / 1760

# Exibe os resultados
print(f"A medida em polegadas é: {polegadas} polegadas")
print(f"A medida em jardas é: {jardas} jardas")
print(f"A medida em milhas é: {milhas} milhas")
