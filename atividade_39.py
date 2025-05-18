# Atividade 39
from math import sqrt
while True:    
    num = int(input("Digite um número inteiro: "))
    if num < 0:
        print("Numero invalido")
    elif num == 0:
        print("Fim!!!")
        break        
    else:
        raiz = (sqrt(num))
        print(raiz)