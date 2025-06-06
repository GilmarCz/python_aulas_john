import numpy as np
# minha resolução
# def matriz_identidade():
#     num = int(input("Digite um número: "))
#     return np.full((num,num),0)
# print(matriz_identidade())


# GPT
def matriz_identidade1():
    num1 = int(input("Digite um número: "))
    return np.identity(num1, dtype=int)  # ou np.eye(num, dtype=int)
print(matriz_identidade1())

# John
def matriz_identidade2():
    num2 = int(input("Digite um número: "))
    return np.eye(num2, dtype=int)  # ou np.eye(num, dtype=int)
print(matriz_identidade2())