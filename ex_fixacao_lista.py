""" 1️⃣ append()
Crie uma lista vazia e use o append() para adicionar os números de 1 a 5.
👉 Exiba a lista final. """
vaziu = []
vaziu.append(1)
vaziu.append(2)
vaziu.append(3)
vaziu.append(4)
vaziu.append(5)
print(vaziu)

""" 2️⃣ insert()
Dada a lista ["maçã", "banana", "laranja"], insira a palavra "abacaxi" na posição 1.
👉 Exiba a nova lista. """
frutas=["maça", "banana", "laranja"]
frutas.insert(0,"abacaxi")
print(frutas)

""" 3️⃣ extend()
Crie duas listas: lista1 = [1, 2] e lista2 = [3, 4, 5]. Use extend() para unir as duas.
👉 Mostre o resultado final. """
lista1 = [1, 2]
lista2 = [3, 4, 5]
lista1.extend(lista2)
print(lista1)

""" 4️⃣ remove()
Dada a lista [10, 20, 30, 20, 40], remova a primeira ocorrência do número 20.
👉 Exiba a lista após a remoção. """
ocorrencia = [10, 20, 30, 20, 40]
ocorrencia.remove(20)
print(ocorrencia)

""" 5️⃣ pop()
Dada a lista [5, 10, 15, 20], use pop() para:
Remover o último elemento
Depois, remover o item da posição 1
👉 Mostre a lista após cada remoção. """
possicao = [5, 10, 15, 20]
possicao.pop(3)
print("Lista apos a remoção da ultima possição:", possicao)
possicao.pop(1)
print("Lista apos a remoção da possição 1:", possicao)

""" 6️⃣ clear()
Crie uma lista com nomes quaisquer e depois use clear() para esvaziá-la.
👉 Mostre a lista antes e depois. """
# Criar uma lista com nomes
nomes = ["Maria", "João", "Ana", "Pedro", "Carla"]
# Mostrar a lista antes de usar clear()
print("Lista antes de clear():", nomes)
# Usar clear() para esvaziar a lista
nomes.clear()
# Mostrar a lista depois de usar clear()
print("Lista depois de clear():", nomes)

""" 7️⃣ index()
Dada a lista ['a', 'b', 'c', 'd'], descubra a posição da letra 'c'.
👉 Mostre o índice encontrado."""
alpha = ['a', 'b', 'c', 'd']
# alpha.index('c')
posicao_c = alpha.index('c')
print(f"A letra 'c' está na posição: {posicao_c}")

""" 8️⃣ count()
Quantas vezes o número 7 aparece na lista [7, 1, 7, 3, 7, 5]?
👉 Use count() e mostre o resultado. """
sete = [7, 1, 7, 3, 7, 5]
print("O número 7 aparece na lista:", sete.count(7), "vezes")

""" 9️⃣ sort()
Ordene a lista [12, 4, 19, 1, 8]:
Primeiro em ordem crescente
Depois em ordem decrescente
👉 Mostre as duas versões da lista. """
ordene = [12, 4, 19, 1, 8]
ordene.sort()
print("ordem crescente: ",ordene)
ordene.sort(reverse=True)
print("ordem decrescente: ",ordene)

""" 🔟 reverse()
Crie uma lista com os números de 1 a 5 e use reverse() para inverter a ordem.
👉 Exiba a lista final. """
inverso = [1, 2, 3, 4, 5]
print("Ordem normal; ", inverso)
inverso.reverse()
print("Ordem invertida; ", inverso)