import numpy as np
def criar_array():
    lista_numeros = [1,2,3,4,5,6]
    
    array_1d = np.array(lista_numeros)
    print(array_1d)
criar_array()

# resolução John
# Cria a função que recebe uma lista
def criar_array1(lista):
    return np.array(lista)
    numeros = [1,2,3,4,5,6]
    print(criar_array1(numeros))
