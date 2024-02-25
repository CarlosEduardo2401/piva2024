from datetime import datetime

def calcular_idade(data_nascimento, data_atual):
    delta = data_atual - data_nascimento

    # Converte a diferença para anos, meses e dias
    idade_anos = delta.days // 365
    idade_meses = (delta.days % 365) // 30
    idade_semanas = delta.days // 7
    idade_dias = delta.days

    return idade_anos, idade_meses, idade_semanas, idade_dias

def main():
    try:
        # Solicita ao usuário que insira a data de nascimento (formato: dd/mm/aaaa)
        data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

        # Converte a string de data de nascimento para um objeto datetime
        data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

        # Obtém a data atual
        data_atual = datetime.now()

        # Calcula a idade
        idade_anos, idade_meses, idade_semanas, idade_dias = calcular_idade(data_nascimento, data_atual)

        # Exibe os resultados
        print(f"A idade é: {idade_anos} anos")
        print(f"A idade em meses é: {idade_meses} meses")
        print(f"A idade em semanas é: {idade_semanas} semanas")
        print(f"A idade em dias é: {idade_dias} dias")

    except ValueError:
        print("Formato de data incorreto. Certifique-se de seguir o formato dd/mm/aaaa.")

if __name__ == "__main__":
    main()
