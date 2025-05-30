agenda = {}

def agenda_telefonica(minha_agenda):
    while True:
        print("--- Agenda Telefonica ---")
        print("- - Digite uma opção: - -")
        opcao = input("Comando (1 Busca | 2 Adiciona | 3 Sair): ")
        if opcao == "1":
            nome = input("Nome: ")
            if nome in agenda:
                print(f"Número: " + agenda[nome])
            else:
                print("Não encontrado o numero!!!")
        elif opcao == "2":
            nome = input("Nome: ")
            numero = input("Número: ")
            agenda[nome] = numero
            print("Número adicionado!")
        elif opcao == "3":
            print("Saindo!")
            break
        else:
            print("Comando invalido!!!\nUse ( 1 | 2 | 3 )")
            
agenda_telefonica(agenda)