destino = input("Digite o destino da viagem (Norte, Nordeste, Centro-Oeste ou Sul): ")
tem_volta = input("A viagem inclui retorno? (S/N): ")

if destino == "Norte":
    if tem_volta == "S":
        preco_passagem = 900
    else:
        preco_passagem = 500
elif destino == "Nordeste":
    if tem_volta == "S":
        preco_passagem = 650
    else:
        preco_passagem = 350
elif destino == "Centro-Oeste":
    if tem_volta == "S":
        preco_passagem = 600
    else:
        preco_passagem = 350
elif destino == "Sul":
    if tem_volta == "S":
        preco_passagem = 550
    else:
        preco_passagem = 300
else:
    print("Destino inválido. Por favor, tente novamente.")
    exit()

print(f"Preço da passagem: R$ {preco_passagem:.2f}")
