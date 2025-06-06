# Atividade 27
preco = float(input("Preço: R$ "))
if preco <= 50:
    print("Categoria Econômica")
elif preco > 50 and preco <= 100:
    print("Categoria Intermediária")
else:
    print("Categoria Premium")