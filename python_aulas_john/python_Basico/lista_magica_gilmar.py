# Chegou a hora de colocar a mão na massa! 🚀 📢 

# Vocês já aprenderam os principais métodos de listas em Python — agora é o momento de aplicar esse conhecimento em um projeto prático e interativo. 
 
# Vamos criar um programa que simula uma Lista Mágica 🪄 — um gerenciador onde o usuário pode adicionar, remover, ordenar e consultar os itens da lista usando tudo que aprendemos em aula.
# 🎯 Desafio: "Lista Mágica do Usuário"
# 🧠 O que você deve fazer?
# Você vai desenvolver um programa interativo em Python que:
# Permite ao usuário criar e manipular uma lista como quiser (compras, tarefas, músicas, filmes, personagens... você escolhe o tema!).
# Usa pelo menos 8 métodos de lista aprendidos em aula.
# Possui um menu para o usuário escolher as ações.
# Mostra a lista sempre que for solicitada.
# Apresenta mensagens amigáveis e trata erros de forma simples (como tentar remover algo que não existe).
# 📌 Funcionalidades obrigatórias (mínimo 8):
# Adicionar um item à lista (append())
# Inserir item em uma posição específica (insert())
# Unir duas listas (extend())
# Remover um item da lista (remove())
# Remover por índice ou o último item (pop())
# Esvaziar toda a lista (clear())
# Mostrar a posição de um item (index())
# Contar quantas vezes um item aparece (count())
# Ordenar a lista (sort())
# Inverter a ordem da lista (reverse())
# 🛠️ Exemplo de estrutura do menu
# MENU DE OPERAÇÕES
# 1. Adicionar item
# 2. Inserir item em posição
# 3. Adicionar vários itens
# 4. Remover item
# 5. Remover por posição
# 6. Limpar lista
# 7. Ver posição de um item   
# 8. Contar item
# 9. Ordenar lista
# 10. Inverter lista
# 0. Sair
# ✨ Critérios de Avaliação
# Critério	Pontos
# Usou pelo menos 8 métodos corretamente	3.0
# Menu funcional e interativo	2.0
# Tratamento de erros básico	1.0
# Código bem estruturado e comentado	2.0
# Criatividade e personalização	2.0
# Total	10.0
# 🧑‍🎨 Dica de personalização
# Seu projeto pode ser temático! Ex:
# 🎮 Lista de jogos favoritos
# 🛍️ Lista de compras da semana
# 🎵 Playlist dos sonhos
# 🎬 Filmes para assistir
# 🧙 Personagens da sua história de RPG
# Use a criatividade! 🚀
# ✅ Entrega
# Formato: arquivo .py com seu código.
# Envie o caminho do projeto do seu GITHUB ou, se preferir, pelo TEAMS com o nome: lista_magica_gilmar.py 

# criando a lista mágica
lista_compras = []  #aqui a lista magica é criada e esta vazia

while True: # while True: = repete o menu indefinidamente.
    print("Menu - Lista de compra!")
    print("1. Adicionar item") # .append
    print("2. Inserir item em posição") # .insert
    print("3. Adicionar vários itens") # .extend
    print("4. Remover item pelo nome") # .remove
    print("5. Remover item pela posição") # .pop
    print("6. Limpar lista") # .clear
    print("7. Ver posição de um item") # .index
    print("8. Contar quantas vezes um item aparece") # .count
    print("9. Ordenar lista") # .sort
    print("10. Inverter lista") # .reverse
    print("11. Ver lista atual")
    print("0. Sair") # break encerrar o programa
    
    opcao = input("Escolha uma opção: ") # input
    
# codificação das opções
    # opção 1 append
    if opcao == "1":
        item = input("Digite o nome do item para adicionar: ") # criado a variavel item junto com a função input para adicionar novo item
        lista_compras.append(item) # usado a função append na lista para adcionar o novo item digitado no final da lista
        print("Item adcinado com sucesso!") # mostra que o item foi adicionado na lista
        
    # opção 2 insert
    elif opcao == "2":
        item = input("Digite o nome do item: ") # criado a variavel item para adicionar novo item
        pos = int(input("Digite a posição (numero): "))  # criado a variavel pos para determinar a posição do novo item, função int para deteminar que o número tem que ser inteiro e o input para adcionar o mesmo
        lista_compras.insert(pos, item) # função insert para inserir o item na posição determinada
        print("Item inserido na posição:" , pos)
        
    # opção 3 extend (varios itens)
    elif opcao == "3":
        itens = input("Digite os itens separados por virgula ( , ): ") # criado a variavel itens para adicionar novos itens
        lista_compras.extend([item.strip() for item in itens.split(",")]) # extend adiciona vários itens de uma vez no final de uma lista
        # strip remove espaços em branco no início e fim de uma string (texto), for e in "repetir" algo (laço de repetição) percorre uma lista um a um
        # split divide um texto em partes usando um separador " , "
        # resumo:
        # split(",") → quebra o texto em lista: ["arroz", " leite", " pão"]
        # for item in ... → percorre cada item da lista
        # item.strip() → limpa espaços (fica "leite" em vez de " leite")
        # extend([...]) → adiciona todos esses itens à lista de compras
        print("Itens adicionados à lista!")
        
         # opção 4 remove
    elif opcao == "4":
        item = input("Digite o nome do item para remover: ") 
        if item in lista_compras:
            lista_compras.remove(item) # remove para remover o item digitado
            print("Item removido!") # exibe mensagem 
        else: # caso o item não esteja na lista
            print("Item não encontrado!") # exibe outra mensagem
        
        # opção 5 remover por posição
    elif opcao == "5":
        pos = int(input("Digite a posição do item que deseja remover: ")) 
        # if, else	Controla o fluxo com condições
        if pos < len(lista_compras): # len retorna o tamanho da lista (quantos itens ela tem)
            removido = lista_compras.pop(pos) # pop remove o último item da lista pop(pos) remove o item da posição
            print(f"'{removido}' removido da posiçao {pos}.") # Formata strings com variáveis (f-strings)
        else:
            print("Posição não encontrada!!!")# exibe outra mensagem
            
        # opção 6 clear 
    elif opcao == "6":
        lista_compras.clear()
        print("Lista de compras limpa!") # clear limpar a lista
        
        # opção 7 index
    elif opcao == "7":
        item = input("Digite o nome do item: ") 
        if item in lista_compras: # Verifica se "item" está na lista
            print("O item está na posição:", lista_compras.index(item)) # index verifica a  posição do item
        else:
            print("Item não encontrado na lista.") # mensagem que o item não esta na lista
            
        # opção 8 count
    elif opcao == "8":
        item = input("Digite o nome do item: ")
        print("O item aparece", lista_compras.count(item), "vez(es).") # count conta quantas vezes o item aparece na lista
        
        # opção 9 sort
    elif opcao == "9":
        lista_compras.sort() # sort  ordem a lista em ordem alfabetica ou em ordem crescente
        print("Lista ordenada em ordem alfabética!") # retorna a lista em ordem alfabetica
        
        # opção 10 reverse
    elif opcao == "10":
        lista_compras.reverse() # inverte a ordem dos itens na lista, modificando a lista original.
        print("Ordem da lista invertida!") # retorna a lista em ordem "inversa"
        
        # opção 11 # enumerate
    elif opcao == "11":
        print("Lista Atual:")
        for i, item in enumerate(lista_compras): # enumetate gera um número automático (o índice) para cada item da lista.
        # resumo:
        # É um laço de repetição que percorre a lista lista_compras e, a cada volta, retorna:
        # i → o índice (posição do item na lista: 0, 1, 2…)
        # item → o valor (o nome do produto que está naquela posição)           
            print(f"{i}. {item}")
        if not lista_compras: # verifica se a lista está vazia, e exibe uma mensagem se estiver.
            print("Lista vazia.") 
        
        # opção 0 break
    elif opcao == "0":
        print("Programa encerrado. Boas compras!")
        break # break sai do laço while True
    
        # Caso nenhuma opção seja valida  
    else: # Executado quando nenhuma opção anterior é válida
        print("Opção inválida. Tente novamente.")