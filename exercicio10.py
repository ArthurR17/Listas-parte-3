produtos = {
    "Açaí de Banana": [20, 15.00],
    "Açaí de Morango": [15, 25.00],
    "Açaí de Granola": [35, 17.00],
    "Açaí de Chocolate": [25, 15.00],
    "Açaí de Baunilha": [30, 20.00]
}

while True:
    print("Opções: ")
    print("1 - Verificar Estoque")
    print("2 - Realizar Venda")
    print("3 - Adicionar no Estoque")
    print("4 - Sair")
    opcao = input("Escolha a opção desejada: ")
    if opcao == "1":
        print("-" * 70)
        print("%25s LISTA DOS PRODUTOS" % " ")
        print("-" * 70)
        print("%1sCÓDIGO" % " ", "%10sPRODUTO" % " ", "%12sQUANTIDADE" % " ", "%10sPREÇO" % " ")
        print("-" * 70)
        print("%1s1" % " ", "%10sAçaí de Banana" % " ", f"%14s{produtos['Açaí de Banana'][0]}" % " ", "%13sR$15,00" % " ")
        print("%1s2" % " ", "%10sAçaí de Morango" % " ", f"%13s{produtos['Açaí de Morango'][0]}" % " ", "%13sR$25,00" % " ")
        print("%1s3" % " ", "%10sAçaí de Granola" % " ", f"%13s{produtos['Açaí de Granola'][0]}" % " ", "%13sR$17,00" % " ")
        print("%1s4" % " ", "%10sAçaí de Chocolate" % "", f"%11s{produtos['Açaí de Chocolate'][0]}" % " ", "%13sR$15,00" % " ")
        print("%1s5" % " ", "%10sAçaí de Baunilha" % " ", f"%12s{produtos['Açaí de Baunilha'][0]}" % " ", "%13sR$20,00" % " ")
        print("-" * 70)
    elif opcao == "2":
        nome = input("Digite o nome do produto que será vendido: ")
        quantidade = int(input("Digite a quantidade a ser vendida por esse produto: "))
        if quantidade <= produtos[nome][0]:
            produtos[nome][0] -= quantidade
            print(f"Foram vendidos {quantidade} {nome}")
        else:
            print(f"Quantidade inválida! A quantidade máxima que você pode vender é {produtos[nome][0]}")
    elif opcao == "3":
        nome = input("Digite o nome do produto que deseja adicionar ao estoque: ")
        quantidade = int(input("Digite a quantidade a ser adicionado por esse produto: "))
        if quantidade <= 100 and (quantidade + produtos[nome][0] <= 100):
            produtos[nome][0] += quantidade
            print(f"Foram adicionados {quantidade} {nome}")
        else:
            print(f"Quantidade muito alta! Por favor, insira uma quantidade que não ultrapasse 100")
    elif opcao == "4":
        print("Processo encerrado: ")
        break
    else:
        print("Digite uma opção válida")

