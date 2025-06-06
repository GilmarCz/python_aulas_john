import numpy as np

rng = np.random.default_rng() # criada para ser chamada a variavel em precisar digitar todo método(defaut_rng)

# Criar Array apartir de listas e tuplas
lista_py = [1,2,3,4,5,6]
print(lista_py)
array_1d = np.array(lista_py) # np.array converte listas e tuplas em array (arranjo)
print(array_1d)

lista2_py = [[1,2,3,4,5,6],[6,5,4,3,2,1]]
print(lista2_py)
array_2d = np.array(lista2_py) # np.array converte listas e tuplas em array (arranjo)
print(array_2d)

# Tuplas
tupla = (1,2,3,4,5,6,7,8,9,10)
array_tupla = np.array(tupla) # np.array converte listas e tuplas em array (arranjo)
print(array_tupla)

# np.zero | cria uma array preenchida por zeros
zero_array = np.zeros((2,3)) # duas linhas e tres colunas
zero1_array = np.zeros((3,3)) # tres linhas e tres colunas
print(f"Array de zero:\n {zero_array},int") # transforma em inteiros
print(f"Array de zero:\n {zero1_array}")

# np.ones | cria array preenchida por 1
one_array = np.ones((2,3),int)
print(one_array)

# np.full | cria array preenchida com números especificos
full_array = np.full((2,4),7.5)
print(full_array)

# np.arange | 
array_arrange = np.arange(0,10,2) # vai contar do 0 até 9 de 2 em 2 (0 2 4 6 8)
print(array_arrange)

array_float_arange = np.arange(0.0,1.0,0.25) # vai contar do 0 até 1 de 0,25 em 0,25 (0 0,25 0,5 0,75)
print(array_float_arange)

# Array de números aleatórios
array_aleatorios = rng.random((2,5)) #float
print(array_aleatorios)
array_aleatorios1 = rng.integers(low=0, high=100, size=(2, 5))  #  int inteiros de 0 a 99
print(array_aleatorios1)

# Indices en NumPy
# indice vetor
array_indice = np.array([1,2,5,9,8])
print(f"elemento 0: {array_indice[0]}") # elemento 0: 1
print(f"elemento 3: {array_indice[3]}") # elemento 3: 9

# indice matriz
array_indice1 = np.array([[1,2,5,9,8],[5,9,8,7,6]])
print(f"elemento na linha 0, coluna 2: {array_indice1[0,2]}") # elemento na linha 0, coluna 2: 5

# Slicing
arr2d = np.array([[1, 2, 3, 4],
                [5, 6, 12, 13],
                [14, 7, 15, 16]])
fatia2d_a = arr2d[:2, 1:3] # [:2, 1:3] :2 seria linha e 1:3 coluna
print(fatia2d_a)
# Saida:
# [[ 2  3]
#  [ 6 12]]

# Operações Matemaaticas:
array_a = np.array([1,3,5,8])
array_b = np.array([2,3,4,5])

# Adição
soma = array_a + array_b
print(soma)

# Subtração
menos = array_a - array_b
print(menos)

# Multiplicação
vezes = array_a * array_b
print(vezes)

# Divisão
divisao = array_a / array_b
print(divisao)

# Copy e View   # view é um espelho
precos = np.array([180.00,10.99,20.50])
print(f"Preços: {precos}")

precoAjustado = precos
print(precos[0] * 2)

# copy faz uma copia, não altera o original
precoAjustado1 = precos.copy()
print(precoAjustado1)

# Iteração
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 25, 35])

for n in array:
    print(f"Valor: {n} ")