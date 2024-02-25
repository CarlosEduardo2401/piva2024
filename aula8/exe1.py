# Função para ler um nome
def ler_nome(tipo_nome):
    return input(f"Digite o {tipo_nome} da pessoa: ")

# Função principal
def main():
    # Ler os nomes separadamente
    primeiro_nome = ler_nome("primeiro nome")
    nome_do_meio = ler_nome("nome do meio")
    sobrenome = ler_nome("sobrenome")

    # Exibir o nome completo
    nome_completo = f"{primeiro_nome} {nome_do_meio} {sobrenome}"
    print("Nome completo:", nome_completo)

# Chamar a função principal
main()
