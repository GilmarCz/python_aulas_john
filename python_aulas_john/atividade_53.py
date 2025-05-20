# Atividade 53
import random
saldo = random.randint(1, 100) * 10
print(f"Saldo disponível: R${saldo:.2f}")
while True:
    saque = int(input("Quanto você quer sacar? "))
   
    if saque % 10 != 0:
        print("Valor inválido! O saque deve ser múltiplo de R$10,00.")
    elif saque > saldo:
         print(f"Saldo insuficiente. Seu saldo é R${saldo:.2f}")
    elif saque <= 0:
        print("Valor inválido! Digite um valor positivo.")
    else:
        saldo -= saque
        print(f"Saque de R${saque:.2f} realizado com sucesso!")
        print(f"Novo saldo: R${saldo:.2f}")
        break