# Solicita ao usuário que insira a altura de cada degrau em centímetros
altura_degrau_cm = float(input("Digite a altura de cada degrau em centímetros: "))

# Solicita ao usuário que insira a altura desejada em metros
altura_desejada_metros = float(input("Digite a altura desejada que você deseja alcançar (em metros): "))

# Converte a altura desejada para centímetros
altura_desejada_cm = altura_desejada_metros * 100

# Calcula quantos degraus o usuário deverá subir
degraus_necessarios = altura_desejada_cm / altura_degrau_cm

# Exibe o resultado
print(f"Você precisará subir {degraus_necessarios:.2f} degraus para alcançar a altura desejada.")
