# Solicita ao usuário que insira a hora no formato de hora e minutos
hora_digitada = input("Digite a hora no formato de hora e minutos (por exemplo, 4,30 para quatro e meia): ")

# Divide a string em horas e minutos
hora, minutos = map(float, hora_digitada.split(','))

# Verifica se os minutos estão dentro do intervalo correto (0 a 60)
if 0 <= minutos <= 60:
    # Calcula a hora digitada apenas em minutos
    hora_em_minutos = hora * 60 + minutos

    # Exibe o resultado
    print(f"A hora digitada em minutos é: {hora_em_minutos} minutos")
else:
    print("Os minutos devem estar no intervalo de 0 a 60.")
