import numpy as np
def somar_matrizes():
    try:
        array_a = np.array([1,3,5,8])
        array_b = np.array([2,3,4,5])
        soma = array_a + array_b
        print("Soma das matrizes:", soma)
    except Exception as e:
        print(f"Erro ao somar os arrays: {e}")    
somar_matrizes()

# resolução John
def soma(matriz1, matriz2):
    if np.shape(matriz1) == np.shape(matriz2):
        return matriz1 + matriz2
    else:
        return "Erro: as matrizes devem ter o mesmo tamanho."
    
m1 = np.array([[1,2],[3,4]])
m2 = np.array([[5,6],[7,8]])

print(soma(m1, m2))