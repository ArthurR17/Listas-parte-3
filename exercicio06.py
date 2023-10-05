produtos = {
    "Ração": [2000, 495.00],
    "Escova": [50, 32.00],
    "Touca": [1500, 45.00],
    "Vasilha de Água": [375, 27.50],
    "Coleira": [400, 80.00]
}

for c, v in produtos.items():
    print(f"{c} | Quantidade: {v[0]} | Valor: {v[1]: .2f}")