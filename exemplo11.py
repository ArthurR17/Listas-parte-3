paises = {
    "Brasil": "sul-americano",
    "Chile": "sul-americano",
    "EUA": "norte-americano",

}

while True:
    pais = input("Digite o nome do país: ")
    if pais == "fim":
        break
    continente = input(f"Digite o nome do continente do {pais}: ")

    paises.update({pais: continente})

for c, v in paises.items():
    print(f"País: {c} | Continente: {v}")