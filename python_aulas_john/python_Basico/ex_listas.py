""" # Listas
frutas = ["maça", "banana", "laranja", "melancia", "tomate", 25, True, 1/2]
#Metodo de lista para adicionar um item ao final da lista
#array.append()
frutas.append(False)
print(frutas)

#Insere um item na posição especificada.
#array.insert(1, 10)
frutas.insert(1,10)

lista = ["maça", "banana", "laranja"]
print(lista[0])  # Saída: maça

for fruta in lista:  
    print("Fruta:", fruta)

# Saída    
#Fruta: maça
#Fruta: banana
#Fruta: laranja """

# .append
""" frutas.append("uva") # Adiciona ao final: ['maçã', 'banana', 'laranja', 'uva'] """


# .clear
""" lista = [1,2,3,4,5]
lista.clear """

# .count
""" lista = [1,1,1,2,2,2,2,3,4,5,1]
print(lista.count(1)) """

# .copy  faz uma copia da lista

# .index identifica a posição na lista
""" indice = frutas.index("pera") # Retorna o índice da primeira ocorrência: 1 """

