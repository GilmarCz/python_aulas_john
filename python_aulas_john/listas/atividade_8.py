import re
def verifica_senha():   
    senhas = [] 
    while len(senhas) < 5:
        cadastra_senha = input(f"Digite a {len(senhas)+1}ª senha (8 caracteres com número): ")
        temNumero = re.search("[0-9]",cadastra_senha)
        if len(cadastra_senha) < 8:
            print("Erro, tente novamente!\n sua senha deve ter 8 caracteres")            
        elif temNumero == None:    
            print("Erro, tente novamente!\n sua senha deve ter pelo menos um número")
        else:
            senhas.append(cadastra_senha) 
            print(f"Senha cadastrada com sucesso! ({len(senhas)}/5)") 
    print(senhas)        
verifica_senha()

# import re
# def verifica_senha():   
#     senhas = [] 
#     while len(senhas) < 5:
#         cadastra_senha = input(f"Digite a {len(senhas)+1}ª senha (8 caracteres com número): ")
#         
#         if len(cadastra_senha) >= 8 and re.search("[0-9]",cadastra_senha) != None:
#              senhas.append(cadastra_senha)  
#         else:
#              print("Senha invalida")      
#     #aqui é só para mostrar a sequencia de senhas válidas:        
#     print("Senhas validas:") 
#     i = 0
#     while i < len(senhas):
#         print(senhas(i))
#         i += 1
# verifica_senha()