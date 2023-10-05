contatos = {
    "José Carlos": "jcarlo@gmail.com",
    "Dayse Melo": "dmelo@terra.com.br",
    "Ana Silva": "asilva@gmail.com",
    "Fábio Moura": "fmoura@gmail.com",
    "Ivan Klouse": "iklouse@ig.com.br",
    "Luísa Fontoura": "Lfontoura@bol.com.br"
}

print("Opções: ")
print("1 - Adicionar contato")
print("2 - Buscar contato")
print("3 - Listar contato")
print("4 - Remover contato")
print("5 - Sair")
while True:
    opcao = input("Escolha a opção desejada: ")
    if opcao == "1":
        nome = input("Digite o nome do contato que deseja adicionar: ")
        email = input("Digite o email do contato que deseja adicionar: ")
        contatos[nome] = email
        print(f"Contato {nome} adicionado com sucesso")
    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja achar: ")
        if nome in contatos:
            print(f"Email de {nome}: {contatos[nome]}")
        else:
            print(f"Contato {nome} não econtrado!")
    elif opcao == "3":
        for c, v in contatos.items():
            print(f"Nome: {c} | Email: {v}")
    elif opcao == "4":
        nome = input("Digite o nome do contato que deseja remover: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato {nome} removido")
        else:
            print(f"Contato {nome} não econtrado!")
    elif opcao == "5":
        print("Processo encerrado")
        break
    else:
        print("Opção inválida")
