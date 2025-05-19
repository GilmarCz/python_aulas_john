# def mesaXadrez(tamanho):
#     for linha in range(tamanho):
#         # Alterna entre começar com 1 ou 0 a cada linha
#         if linha % 2 == 0:
#             print('10' * (tamanho // 2) + '1' * (tamanho % 2))
#         else:
#             print('01' * (tamanho // 2) + '0' * (tamanho % 2))

# # Solicita o tamanho ao usuário
# num = int(input("Qual o tamanho? "))
# mesaXadrez(num)

num = int(input("Qual o tamanho? "))
def xadrez(tamanho):
    linha = 0
    while linha < tamanho:
        coluna = 0
        linha_texto = ""
        while coluna < tamanho:
            if (linha + coluna) % 2 == 0:
                linha_texto += "1"
            else:
                linha_texto += "0"
            coluna +=1
        print(linha_texto)
        linha += 1
xadrez(num)