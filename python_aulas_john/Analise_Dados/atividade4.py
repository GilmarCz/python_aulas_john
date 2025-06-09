import numpy as np

def gerrar_array_intervalo():
    n1 = int(input("Digite um número inteiro: "))
    n2 = int(input("Digite outro número inteiro: "))

    try:
        if n1 <= n2:
            array1 = np.arange(n1,n2+1)  
            print(array1)
        else:
            print("Digite novamente, primeiro o menor depois o maior")
        
    except ValueError:
        print("Errado seu enegumero, digite um NÚMERO!!!!\nSeu Idiota")
gerrar_array_intervalo()