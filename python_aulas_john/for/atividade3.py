numeros = [-8, -6, -1, 0, 2, 5, 3]

def Soma_Positivos(lista: list):
    soma = 0
    for i in lista:
        if i > 0:
            soma += i
    return soma

print(Soma_Positivos(numeros))         