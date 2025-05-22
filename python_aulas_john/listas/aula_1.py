# # Criar uma lista
# minha_Lista = [10, 20, 30]

# # Acessando elementos da lista por meio dos indices
# print(minha_Lista[0])
# print(minha_Lista[1])
# print(minha_Lista[2])

# # Trabalhando com elementos da lista
# resultado = minha_Lista[0] + minha_Lista[2]
# print(resultado)

# # Tamanho da lista
# tamanho_da_lista = len(minha_Lista)
# print(f"Minha lista tem {tamanho_da_lista} de tamanho")

# Prática
# lista1 = [1, 2, 3, 4, 5]

# while True:
#     troca = int(input("Digite um índice ou -1 para sair: "))
#     if troca == -1:
#         break
    
#     if troca < 0 or troca >= len(lista1):
#         print("Índice inválido! Digite um valor entre 0 e", len(lista1)-1)        
    
#     valor = int(input("Digite um novo valor: "))
#     lista1[troca] = valor
#     print("Lista atualizada:", lista1)
    
# lista1 = [1, 2, 3, 4, 5]

# while True:
#     print("Lista atual: ",lista1)
#     troca = int(input("digite um índice ou -1 para sair: "))
#     if troca == -1:
#         print("Programa encerrado")
#         break
#     if 0 <= troca < len(lista1):
#      valor = int(input("digite um novo valor: "))   
#      lista1[troca] = valor
#     else:
#         print("Indice invalido, tente novamente:")
        
# print(lista1)
    
# Fatiar lista
# letras = ['a','b','c','d','e','f']
# print(letras[1:4]) # corta do elemento 1 ao elemento 4 --> ['b', 'c', 'd']
# print(letras[:3]) # corta do início até o 3-1 --> ['a', 'b', 'c']
# print(letras[3:]) # do índice 3 até o final --> ['d', 'e', 'f']
# print(letras[::2]) # todos, com passo 2 (pula de 2 em 2) --> ['a', 'c', 'e']
# print(letras[::-1]) # lista invertida --> ['f', 'e', 'd', 'c', 'b', 'a']

# Adicionar itens a lista
# numeros = []
# numeros.append(5)
# numeros.append(2)
# numeros.append(6)
# numeros.append(10)
# numeros.append(1)
# print(numeros)

# Prática
# pergunta = int(input("Quantos itens serão adicionados? "))
# lista = []
# controle = 0
# while controle < pergunta:
#    nun = int(input(f"Digite o {controle+1}° número: ")) 
#    lista.append(nun)
#    controle += 1
#    print(lista)
# print(f"Lista completa: {lista}")

# Adicionar itens em um "lugar" especifico
# numeros = []
# numeros.append(5)
# numeros.append(2)
# numeros.append(6)
# numeros.append(10)
# print(numeros)
# numeros.insert(1,50)
# print(numeros)
# numeros.insert(0,0)
# print(numeros)
# numeros.insert(3,33)
# print(numeros)

# # Remover itens
# numeros.pop(2)
# print(numeros)
# num_del = numeros.pop(0)
# print(numeros)

# # Remover o valor de um elemento da lista
# numeros.remove(33)
# print(numeros)
# numeros.insert(10,"Gil")
# print(numeros)
# numeros.remove("Gil")
# print(numeros)

# Pratica
escolha = int(input("Escolha uma opção: \n 1-Para adicionar item \n 2-Para excluir item \n 0-Para sair \n OPÇÂO:"))
lista = [1]
controle = 1
while True:
    if escolha == 1:
        print("Adicionar +1 \n", lista)
        lista.append(controle + 1)
        controle += 1
    elif escolha == 2:
        print("Excluir -1 \n", lista)
        if controle < 0:
            print("Lista vazia, adicione 1 na lista")
        else:
            lista.pop(controle - 1)
            controle -= 1
    elif escolha == 0:
        print("Sair \n", lista)
        break
    else:
        print("Opção invalida! Tente: 1 , 2 ou 0 \n", lista)
        
print(lista)