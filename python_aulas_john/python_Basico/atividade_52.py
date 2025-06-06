# Atividade 52
import random
n_secreto = random.randint(1, 100)
tentativas = 0
print("Adivinhe um número entre 1 e 100 ")
while True:
    palpite = int(input("Qual é seu número? ")) 
    tentativas += 1   
    if palpite == n_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas!")
        break
    elif palpite < n_secreto:
            print("O número secreto é maior. Tente novamente!")
    else:
            print("O número secreto é menor. Tente novamente!")