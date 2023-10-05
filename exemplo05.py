contatos = {
    "João": "joao.gomes@gmail.com",
    "Ana Rosa": "rosa.ana@terra.com.br",
    "Luis": "luis45@gmail.com"
}

nome = input("Digite o nome a ser pesquisado: ")
if nome in contatos:
    print(f"Email do (a) {nome}: {contatos[nome]}")
else:
    print(f"Contato {nome} não econtrado!")