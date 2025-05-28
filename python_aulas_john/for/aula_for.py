# # for
# lista = ["Maria", "Madalena", "Pedro", "Paulo", "Alex", "L"]
# for nome in lista:
#     print(nome)
#     if len(nome) > 2:
#         print(f"O {nome} tem mais que 2 caracteres")
#     else:
#         print(f"O {nome} tem menos que 2 caracteres")
        
# # range no for
# for i in range(100): # faz a contagem do 0 a 99 (conta o indice)
#     print(i)
# for j in range(5,20): # faz a contagem do 5 a 19 (conta o indice)
#     print(j)
# for k in range(0,10,2): # faz a contagem 0 2 4 6 8 pulando de 2 em 2
#     print(k)
    
# # criando uma lista apartir do range
# numero = list(range(3,15))
# print(numero)
# print(numero[5])
# for i in numero:
#     print(i)

# count() conta quantas vezes uma string ou interio tem dentro de um conjunto de dados
minha_string = "Quantas madeiras um esquilo poderia empilhar se um esquilo pudesse empilhar madeiras"
print(minha_string.count("a")) # Vai contar quantas vezes a letra 'a' aparece (9 vezes)

minha_lista = [1,2,3,5,6,6,9,9,8]
print(minha_lista.count(6)) # Vai contar quantas vezes o 6 aparece (2 vezes)

# Replace substitui uma string por outra string
minha_palavra = "Oi, oi, oi amigos"
nova_palavra = minha_palavra.replace("Oi","Olá")
print(nova_palavra) # Olá, oi, oi amigos