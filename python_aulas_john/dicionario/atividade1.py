# Função principal que gerencia a agenda telefônica
def agenda_telefonica(minha_agenda):
    agenda = {}  # Cria um dicionário vazio chamado 'agenda' que armazenará os contatos (nome: número)
    while True:  # Laço infinito para manter o programa rodando até que o usuário decida sair
        print("--- Agenda Telefonica ---")  # Título da agenda
        print("- - Digite uma opção: - -")  # Orientação ao usuário
        opcao = input("Comando (1 Busca | 2 Adiciona | 3 Sair): ")  # Lê a opção do usuário
        
        if opcao == "1":  # Se o usuário escolher buscar um número
            nome = input("Nome: ")  # Solicita o nome a ser buscado
            if nome in agenda:  # Verifica se o nome está na agenda
                print(f"Número: " + agenda[nome])  # Mostra o número correspondente
            else:
                print("Não encontrado o numero!!!")  # Mensagem de erro caso o nome não exista
        
        elif opcao == "2":  # Se o usuário escolher adicionar um novo contato
            nome = input("Nome: ")  # Solicita o nome do contato
            numero = input("Número: ")  # Solicita o número do contato
            agenda[nome] = numero  # Adiciona o par nome:número no dicionário
            print("Número adicionado!")  # Confirmação para o usuário
        
        elif opcao == "3":  # Se o usuário escolher sair do programa
            print("Saindo!")  # Mensagem de encerramento
            print(agenda)  # Mostra a agenda
            break  # Encerra o laço e termina a função
        
        else:  # Caso o usuário digite uma opção inválida
            print("Comando invalido!!!\nUse ( 1 | 2 | 3 )")  # Mensagem de erro
            

# Chama a função
agenda_telefonica()
