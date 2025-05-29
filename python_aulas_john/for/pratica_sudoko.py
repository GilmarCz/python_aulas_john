sudoku = [  # Criação de uma matriz 9x9 representando um tabuleiro de Sudoku
    [9,0,0,0,8,0,3,0,0],
    [0,0,0,2,5,0,7,0,0],
    [0,2,0,3,0,0,0,0,4],
    [0,9,4,0,0,0,0,0,0],
    [0,0,0,7,3,0,5,6,0],
    [7,0,5,0,6,0,4,0,0],
    [0,0,7,8,0,3,9,0,0],
    [0,0,1,0,0,0,0,0,1],
    [3,0,0,0,0,0,0,0,2]
]

def imprimir_sudoku(tabuleiro):  # Criação da função para imprimir a matriz formatada
    for linha in tabuleiro:  # Percorre cada linha da matriz
        linha_formatada = ""  # Cria uma string vazia para armazenar os elementos formatados da linha
        for i in linha:  # Percorre cada elemento da linha
            if i == 0:  # Se o valor for 0 (posição ainda não preenchida no Sudoku)
                linha_formatada += "_ "  # Adiciona um sublinhado e um espaço à string
            else:  # Caso contrário (posição preenchida com número)
                linha_formatada += str(i) + " "  # Converte o número para string e adiciona à string formatada
        print(linha_formatada)  # Imprime a linha formatada

imprimir_sudoku(sudoku)  # Chamada da função com a matriz Sudoku como argumento


#Resolução John

# for linha in sudoku:
#     for item in linha:
#         if item == 0:
#             print("_ ",end="")
#         else:
#             print(item,"",end="")
#     print("")