ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365.25
idade_semanas = idade_anos * 52.1775


print(f"A idade em anos é: {idade_anos} anos")
print(f"A idade em meses é: {idade_meses:.2f} meses")
print(f"A idade em dias é: {idade_dias:.2f} dias")
print(f"A idade em semanas é: {idade_semanas:.2f} semanas")
