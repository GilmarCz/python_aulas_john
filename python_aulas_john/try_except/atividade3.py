# Lista de frutas disponíveis
frutas = ["Pera", "Maçã", "Uva", "Laranja", "Melancia", "Limão", "Abacate"]
i = len(frutas) # Obtém o tamanho da lista (quantidade de frutas)
try:
    # Solicita ao usuário um número correspondente ao índice da fruta
    # Mostra automaticamente o intervalo válido baseado no tamanho da lista (0 a i-1)
    indice = int(input(f"Digite um número entre 0 e {i-1} para exibir a fruta da lista: "))    
    # Se a conversão para int for bem-sucedida, tenta acessar o elemento na lista
    print(frutas[indice])  # Acessa e exibe a fruta no índice digitado

except ValueError:  # Captura erro se o usuário digitar algo que não pode ser convertido para número inteiro
       print("Erro!!! Entrada inválida! Por favor, digite um número.")

except IndexError: # Captura erro se o número digitado estiver fora dos índices válidos da lista
    # Mostra novamente o intervalo correto para ajudar o usuário
    print(f"Erro!!! Número fora do intervalo. Digite um valor entre 0 e {i-1}.")