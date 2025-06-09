import numpy as np

# minha primeira tentativa de resolução 
# def estatistica_array():
#    array_e= np.array([1,2,5,9,8])
#    tam = len(array_e)
#    for i == tam:
#        soma += array_e[i]
    
#        media = soma/tam
# estatistica_array()

# porém não é para usar nem for ou while
# import numpy as np

# def estatistica_array():
#     array_e = np.array([1, 2, 5, 9, 8])
#     print(f"Tamanho: {array_e.size}")
#     print(f"Soma: {array_e.sum()}")
#     print(f"Média: {array_e.mean():.2f}")

# estatistica_array()

# minha resolução
def estatistica_array():
    array_e = np.array([1, 2, 5, 9, 8])   
    soma = np.sum(array_e)       # ou array.sum() soma
    media = np.mean(array_e)     # ou array.mean() média   
    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")

estatistica_array()

# Resolução John
def estatistica(array):
    soma1 = np.sum(array)
    media1 = np.mean(array)
    return soma1, media1
meu_array = np.array([10,20,30,40,50])
print(estatistica(meu_array))