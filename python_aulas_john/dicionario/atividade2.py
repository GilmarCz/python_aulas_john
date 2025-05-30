# Função principal que gerencia a agenda telefônica
def agenda_telefonica():
    agenda = {} # Cria um dicionário vazio chamado 'agenda' que armazenará os contatos (nome: número)
    while True:# Loop principal do programa - continua até o usuário escolher sair
        print("--- Agenda Telefonica ---")  # Título da agenda
        print("- - Digite uma opção: - -")  # Orientação ao usuário
        opcao = input("Comando (1 Busca | 2 Adiciona | 3 Sair): ")  # Lê a opção do usuário
                
        if opcao == "1": # Se escolheu buscar (opção 1)
            nome = input("nome: ") # Pede o nome para buscar
            if nome in agenda: # Verifica se o nome existe na agenda
                for numero in agenda[nome]: # Se existe, imprime TODOS os números dessa pessoa. Usa um loop for para percorrer a lista de números
                    print(numero)
            else: # Se não existe, mostra mensagem padrão                
                print("nenhum número")        
        
        elif opcao == "2": # Se escolheu adicionar (opção 2)            
            nome = input("nome: ") # Pede o nome da pessoa            
            numero = input("número: ") # Pede o número de telefone            
            
            if nome in agenda: # Verifica se a pessoa já existe na agenda                
                agenda[nome].append(numero) # Se já existe, adiciona o novo número na lista existente
            else:                
                agenda[nome] = [numero]# Se não existe, cria uma nova lista com o primeiro número
                        
            print("Número adicionado!") # Confirma que foi adicionado com sucesso
                
        elif opcao == "3": # Se escolheu sair (opção 3)
            print("saindo...") # Mostra mensagem de saída
            print(agenda)            
            break # Quebra o loop infinito e termina o programa
                
        else: # Se digitou uma opção inválida
            
            print("Comando invalido!!!\nUse ( 1 | 2 | 3 )") # Mostra mensagem de erro

agenda_telefonica() # Chama a função para executar o programa