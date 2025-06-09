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