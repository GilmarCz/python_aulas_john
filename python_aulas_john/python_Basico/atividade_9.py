# Atividade 9
conta = float(input("A conta, é: R$"))
gorjeta = float(input("Gorjeta de:(%) "))
gorj = conta*(gorjeta/100)
contaGorj = conta+gorj
print(f"A sua conta ficou em R${contaGorj}")