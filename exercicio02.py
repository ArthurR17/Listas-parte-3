contatos = {
    "José Carlos": "jcarlo@gmail.com",
    "Dayse Melo": "dmelo@terra.com.br",
    "Ana Silva": "asilva@gmail.com",
    "Fábio Moura": "fmoura@gmail.com",
    "Ivan Klouse": "iklouse@ig.com.br",
    "Luísa Fontoura": "Lfontoura@bol.com.br"
}

nome = input("Digite o nome a ser pesquisado: ")
while True:
    if nome in contatos:
        print(f"Email de {nome}: {contatos[nome]}")
        nome = input("Digite o nome a ser pesquisado: ")
    elif nome == "fim":
        break
    else:
        print(f"Contato {nome} não econtrado!")
        nome = input("Digite o nome a ser pesquisado: ")
