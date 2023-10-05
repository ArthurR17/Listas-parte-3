produtos = {
    "Ração": 513.00,
    "Coleira de Passeio": 60.00,
    "Shampoo": 25.00,
    "Toca de Plástico": 105.00,
    "Cobertor": 86.00,
    "Serviço de Banho": 120.00,
}

nome = input("Digite o nome do produto a ser pesquisado: ")
if nome in produtos:
    print(f"O valor de {nome} é de: R${produtos[nome]}")
else:
    print(f"Produto {nome} não econtrado!")