# Inicializa a lista com o número 1 já presente
lista = [1]

# Define o próximo número a ser adicionado como 2 (já que 1 já está na lista)
proximo_numero = 2

# Início do loop infinito para manter o programa em execução até o usuário decidir sair
while True:
    # Mostra as opções e lê a entrada do usuário como string
    entrada = input("1-Adicionar | 2-Remover | 0-Sair: ")

    # Verifica se o usuário escolheu a opção de adicionar item
    if entrada == "1":
        # Adiciona o próximo número à lista
        lista.append(proximo_numero)
        # Mostra qual número foi adicionado
        print("Adicionado:", proximo_numero)
        # Incrementa o número para a próxima adição
        proximo_numero += 1

    # Verifica se o usuário escolheu a opção de remover item
    elif entrada == "2":
        # Verifica se a lista não está vazia antes de remover
        if lista:
            # Remove o último item da lista e guarda ele na variável 'removido'
            removido = lista.pop()
            # Mostra qual número foi removido
            print("Removido:", removido)
        else:
            # Informa que a lista está vazia e nada pode ser removido
            print("Erro: Lista vazia!")

    # Verifica se o usuário escolheu sair do programa
    elif entrada == "0":
        # Mostra mensagem de saída e exibe o conteúdo final da lista
        print("Saindo... Lista final:", lista)
        # Encerra o loop com break
        break

    # Se a entrada não for 1, 2 ou 0, é considerada inválida
    else:
        # Informa que a entrada foi inválida
        print("Opção inválida! Digite 1, 2 ou 0.")

    # Mostra a lista atual após cada ação
    print("Lista atual:", lista)
