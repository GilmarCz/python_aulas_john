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
# Inicia a lista vazia
# lista = []

# # Controle serve para manter o valor do próximo número a ser adicionado ou o tamanho da lista
# controle = 1

# # Início de um laço infinito que só para quando o usuário escolher sair
# while True:
#     # Mostra o menu de opções e solicita entrada do usuário
#     escolha = input("Escolha uma opção: \n 1-Para adicionar item | 2-Para excluir item | 0-Para sair \n OPÇÂO: ")

#     # Se o usuário escolher "1", será adicionado um novo número à lista
#     if escolha == "1":
#         # Exibe mensagem e a lista atual antes da adição
#         print("Adicionar +1 \n", lista)
#         # Adiciona o próximo número (controle + 1) na lista
#         lista.append(controle )
#         # Atualiza o controle (incrementa 1)
#         controle += 1

#     # Se o usuário escolher "2", será feita uma tentativa de remover o último item da lista
#     elif escolha == "2":
#         # Exibe mensagem e a lista atual antes da remoção
#         print("Excluir -1 \n", lista)
#         # Verifica se o controle é menor que 0 
#         if len(lista) == 0:

#             # Informa que a lista está vazia
#             print("Lista vazia, adicione 1 na lista")
#         else:
#             # Remove o último item da lista com base no índice (controle - 1)
#             lista.pop()
#             # Atualiza o controle (decrementa 1)
#             controle -= 1

#     # Se o usuário escolher "0", o programa encerra
#     elif escolha == "0":
#         # Exibe mensagem de saída e a lista atual
#         print("Sair \n", lista)
        
#         if lista == []:
#             print(f"Lista vázia ",lista)
#         # Interrompe o loop com break    
#         break

#     # Se a entrada for diferente de "1", "2" ou "0", exibe aviso de opção inválida
#     else:
#         print("Opção invalida! Tente: 1 , 2 ou 0 \n", lista)

#     # Exibe a lista atual ao final de cada iteração
#     print(lista)

# lista = []
# while True:
#     opcao = input("O que você quer fazer? + ou - : ")
#     if opcao == "+":
#         if len(lista) == 0:
#             lista.append(1)
#         else:

# Sort - Classificação
# lista = [0,45,68,98,78,65,23,35,54,47,89]
# print(lista)
# lista.sort()
# # Sorted cria uma cópia da lista original em outra variavel
# lista_v2 = sorted(lista)
# print(lista)
# print(lista_v2)

# Prática
# lista = []
# while True:
#     adicionar = int(input("Digite um número e 0 para sair: "))
#     if adicionar == 0:
#         print("Sair")
#         break
#     else:
#         lista.append(adicionar)
#         print(f" Lista na ordem - {lista}")
#         lista_ord = sorted(lista)
#         print(f" Lista ordenada - {lista_ord}")
        
