#lista = [2,8,10,9,1]
# def range(lista):
#     minimo = min(lista)
#     maximo = max(lista)
#     diferenaca = [minimo,maximo]
#     return diferenaca
# resultado = range(lista)
# print(resultado)

lista = [2,8,10,9,1]

def range(lista):
    return max(lista) - min(lista)

print(range(lista))