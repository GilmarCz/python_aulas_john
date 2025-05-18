# Atividade 41
senha = input("Digite sua senha: ")
while True:
    tentativa = input("Digite novamente para confirmar: ")
    if tentativa == senha:
        print("Senha confirmada com sucesso!")
        break  # Sai do loop quando acertar
    else:
        print("As senhas não coincidem. Tente novamente.")

tentativas = 0
while True:
    codigo = input("Digite o PIN: ")
    tentativas += 1
    if codigo == "12345":
        sucesso = True
        break
    if tentativas == 3:
        sucesso = False
        break
    print("Incorreto...Tente Novamente")
    
if sucesso:
    print("PIN correto inserido")
else:
    print("Muitas tentativas")
