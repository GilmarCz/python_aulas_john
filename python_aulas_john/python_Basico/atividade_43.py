# Atividade 43
ano = int(input("Digite um ano: "))
# Encontra o próximo ano bissexto
while True:
    ano += 1
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"O próximo ano bissexto é {ano}")
        break
