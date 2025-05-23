def menu_tarefa():
    tarefas = []
    while True:
        funcao = input("MENU \n 1. Adicionar tarefa\n 2. Remover\n 3. Mostras Tarefas\n 4. Sair\n Opção: ")
        if funcao == "1":
            tarefa_add = input("Digite a tarefa: ")
            tarefas.append(tarefa_add)    
        elif funcao == "2":
            print(tarefas)
            tarefa_rem = input("Digite qual tarefa excluir: ")
            tarefas.remove(tarefa_rem)
        elif funcao == "3":
            print(tarefas)
        elif funcao == "4":
            print(f"Saindo!!!\nSuas tarefas são: {tarefas}")
            break
        else:
            print("Função Invalida!!!\nTente novamente (1 - 2 - 3 - 4)")
menu_tarefa()