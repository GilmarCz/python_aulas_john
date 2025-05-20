# Atividade 33
idade = int(input("Qual é sua idade? "))
if idade >= 5:
    print(f"Ok, você tem {idade} anos")
elif idade < 5 and idade >= 0:
    print(f"Suspeito que você não saiba escrever ...")
else:
    print(f"Isso deve ser um erro ...")
