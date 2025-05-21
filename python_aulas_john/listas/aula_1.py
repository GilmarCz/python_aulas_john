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
    
lista1 = [1, 2, 3, 4, 5]

while True:
    print("Lista atual: ",lista1)
    troca = int(input("digite um índice ou -1 para sair: "))
    if troca == -1:
        print("Programa encerrado")
        break
    if 0 <= troca < len(lista1):
     valor = int(input("digite um novo valor: "))   
     lista1[troca] = valor
    else:
        print("Indice invalido, tente novamente:")
        
print(lista1)
    