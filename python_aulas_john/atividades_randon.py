import re #Biblioteca de Expressôes Regulares
import random #Biblioteca de Numeros Randomicos

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

while True:
    senha = input("Digite uma senha: ")
    temMaiuscula = re.search("[A-Z]",senha)
    temMinuscula = re.search("[a-z]",senha)
    temNumero = re.search("[0-9]",senha)
    if len(senha) < 8:
        print("Precisa de 8 caracteres")
    elif temMaiuscula == None:
        print("Precisa de 1 letra maiuscula")
    elif temMinuscula == None:
        print("Precisa de 1 letra minuscula")
    elif temNumero == None:
        print("Precisa de 1 número")
    else:
        print("Sucesso")
        break