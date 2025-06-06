# Atividade 42
tentativas = 0
while True:
    codigo = input("PIN: ")
    tentativas += 1
    if codigo == "4321":
        print(f"Sucesso, números de tentativas = {tentativas}")
        break
    else:
        print("Tente novamente")