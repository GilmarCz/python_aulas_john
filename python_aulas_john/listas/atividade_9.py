# Errado
# def decrescente():
#     i = 0
#     while True:
#         num = int(input("Digite um número aleatório: "))
#         lista = []
        
#         if num > lista(i-1):
#             lista.append(num)
#         else:
#             lista.append(num)
#             break
#     lista_ordenada = sorted(lista)    
#     print(lista)
#     print(lista_ordenada)
# decrescente()

def crescente():
    lista = []
    
    while True:
        num = int(input("Digite um número aleatório: "))
        
        if not lista:  # Se a lista estiver vazia
            lista.append(num)
        else:
            if num < lista[-1]:  # Se o número for menor que o anterior
                lista.append(num)
                break  # Encerra o loop
            else:
                lista.append(num)
    
    print("\nTodos os números digitados:", lista)
    print("Números em ordem crescente:", sorted(lista))

crescente()

# Resolução John
# def lista_crescente():
#     numeros = []
#     while True:
#         numero = int(input("Digite um número: "))
#         numeros.append(numero)
        
#         if len(numeros) > 1 and numeros[-1] < numeros[-2]:
#             break
#     numeros_ord = sorted(numeros)
#     print("Números digitados (ordem crescente): ", numeros_ord)
    
# lista_crescente()