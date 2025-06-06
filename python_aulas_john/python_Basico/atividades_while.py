# Atividade 38
# while True:
#     controle = input("Você quer continuar? ")
#     if controle == "não":
#         print("Parei!")
#         break
#     else:
#         print("Olá")
        
# Atividade 39
# from math import sqrt
# while True:    
#     num = int(input("Digite um número inteiro: "))
#     if num < 0:
#         print("Numero invalido")
#     elif num == 0:
#         print("Fim!!!")
#         break        
#     else:
#         raiz = (sqrt(num))
#         print(raiz)

# Atividade 40
# num = 5
# print("Contando")
# while True:
#     print(num)
#     num = num - 1
#     if num == 0:    
#         break
# print("Foi!!")

# Atividade 41
# senha = input("Digite sua senha: ")
# while True:
#     tentativa = input("Digite novamente para confirmar: ")
#     if tentativa == senha:
#         print("Senha confirmada com sucesso!")
#         break  # Sai do loop quando acertar
#     else:
#         print("As senhas não coincidem. Tente novamente.")

# tentativas = 0
# while True:
#     codigo = input("Digite o PIN: ")
#     tentativas += 1
#     if codigo == "12345":
#         sucesso = True
#         break
#     if tentativas == 3:
#         sucesso = False
#         break
#     print("Incorreto...Tente Novamente")
    
# if sucesso:
#     print("PIN correto inserido")
# else:
#     print("Muitas tentativas")

# Atividade 42
# tentativas = 0
# while True:
#     codigo = input("PIN: ")
#     tentativas += 1
#     if codigo == "4321":
#         print(f"Sucesso, números de tentativas = {tentativas}")
#         break
#     else:
#         print("Tente novamente")
        
# Atividade 43
# ano = int(input("Digite um ano: "))
# # Encontra o próximo ano bissexto
# while True:
#     ano += 1
#     if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
#         print(f"O próximo ano bissexto é {ano}")
#         break

# Atividade 44
# numero = 2
# while numero <= 30:
#     print(numero)
#     numero += 2
# print("Execução finalizada!!!")

# Atividade 45
# print("Você esta pronto?")
# n = int(input("digite um numero: "))
# while n == 0:
#     print(n)
#     print("Agora!")
#     n = int(input("digite um numero: ")) 
    
# Atividade 46
# n = int(input("Digite um número inteiro: "))
# print(f"Números maiores que 0 e menores que {n}:")
# i = 1
# while i < n:  # Enquanto for menor que n
#     print(i)
#     i += 1  # Incrementa em 1

# Atividade 47
# sup = int(input("Digite um limite superior: "))
# i = 1
# while i <= sup:
#     print(i)
#     i *= 2
# print(f"O limite era: {sup}")

# Atividade 48
# sup = int(input("Digite um limite superior: "))
# multi= int(input("Qual é o multiplicador (maior igual a 2): "))
# i = 1
# while i <= sup:
#     print(i)
#     i *= multi
# print(f"O limite era: {sup}")