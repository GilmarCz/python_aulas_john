# import re #Biblioteca de Expressôes Regulares
# import random #Biblioteca de Numeros Randomicos

# print(re.search("[A-Z]","Senha"))
# print(re.search("[A-Z]","senha"))
# print(re.search("[A-Z]","seNHa"))
# print(re.search("[0-9]","seN1a"))

# numero_secreto = random.randint(1,200)
# print(numero_secreto)

# Atividade 50
# soma = 0
# while soma <= 100:
#     n = int(input("Digite um número: "))
#     soma += n
# print(soma)

# Atividade 51
# senha = input("Digite uma senha: ")
# while True:
    
#     if  (len(senha) >= 8 and re.search(r'[A-Z]', senha) and  # Pelo menos 1 letra maiúscula
#         re.search(r'[a-z]', senha) and  # Pelo menos 1 letra minúscula
#         re.search(r'[0-9]', senha)):
#         print("Logado com sucesso")
#         break
#     else:
#         print("Tente Novamente")
#         senha = input("Digite novamente: ")

# while True:
#     senha = input("Digite uma senha: ")
#     temMaiuscula = re.search("[A-Z]",senha)
#     temMinuscula = re.search("[a-z]",senha)
#     temNumero = re.search("[0-9]",senha)
#     if len(senha) < 8:
#         print("Precisa de 8 caracteres")
#     elif temMaiuscula == None:
#         print("Precisa de 1 letra maiuscula")
#     elif temMinuscula == None:
#         print("Precisa de 1 letra minuscula")
#     elif temNumero == None:
#         print("Precisa de 1 número")
#     else:
#         print("Sucesso")
#         break
    
# Atividade 52
# import random
# n_secreto = random.randint(1, 100)
# tentativas = 0
# print("Adivinhe um número entre 1 e 100 ")
# while True:
#     palpite = int(input("Qual é seu número? ")) 
#     tentativas += 1   
#     if palpite == n_secreto:
#         print(f"Parabéns! Você acertou em {tentativas} tentativas!")
#         break
#     elif palpite < n_secreto:
#             print("O número secreto é maior. Tente novamente!")
#     else:
#             print("O número secreto é menor. Tente novamente!")

# Atividade 53
# import random
# saldo = random.randint(1, 100) * 10
# print(f"Saldo disponível: R${saldo:.2f}")
# while True:
#     saque = int(input("Quanto você quer sacar? "))
   
#     if saque % 10 != 0:
#         print("Valor inválido! O saque deve ser múltiplo de R$10,00.")
#     elif saque > saldo:
#          print(f"Saldo insuficiente. Seu saldo é R${saldo:.2f}")
#     elif saque <= 0:
#         print("Valor inválido! Digite um valor positivo.")
#     else:
#         saldo -= saque
#         print(f"Saque de R${saque:.2f} realizado com sucesso!")
#         print(f"Novo saldo: R${saldo:.2f}")
#         break

# Atividade 54
# import re
# while True:
#     p1 = input("Digite a primeira palavra: ")
#     p2 = input("Digite a segunda palavra: ")
#     if len(p1) == len(p2):
#         print("Ok, obrigado!!!")
#         break
#     else:
#         p1 = input("Digite novamente a primeira palavra: ")
#         p2 = input("Digite novamente a segunda palavra: ")
        
