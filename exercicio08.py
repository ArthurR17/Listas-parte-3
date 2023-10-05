produtos = {
    "Ração Royal Canin - 10kg": ["Pet do Rei", 495.00],
    "Ração Origens - 10kg": ["Walmak", 183.00],
    "Ração Golden Power - 10kg": ["Mercadão das Rações", 180.00],
    "Ração Gran Plus - 10kg": ["Pet do Animal", 274.00],
    "Ração Whiskas - 10kg": ["Paraíso das Rações", 165.00],
}


while True:
    adicionar = input("Deseja adicionar um produto? [S/N]: ")
    if adicionar == "S":
        nome = input("Nome do produto: ")
        loja = input("Nome da loja: ")
        valor = float(input("Valor do produto: "))
        produtos[nome] = [loja, valor]
    elif adicionar == "N":
        break

print("Produtos cadastrados:")
for c, v in produtos.items():
    print(f"{c} | Loja: {v[0]} | Valor: {v[1]: .2f}")