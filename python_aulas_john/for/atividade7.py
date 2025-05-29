# # Resolução John
# mesa = [
#     ["","",""],
#     ["","",""],
#     ["","",""]
#     ]
# contador = 0
# print(F"Tempo: {contador} - Olá jogador 1, comece o jogo com X. BOA SORTE!")
 
# def jogue_o_jogo(mesa,linha,coluna,caracter):
#     mesa[linha][coluna] = caracter
#     exibe_resultado()
#     if contador % 2 != 0:
#         jogador = "1 (x)"
#     else:
#         jogador = "2 (O)"
       
#     print(f"Tempo {contador} - Ótimo jogada, agora é a vez do jogador {jogador}")
#     print("")
 
# def exibe_resultado():
#     for linhas in mesa:
#         for items in linhas:
#             if items == "":
#                 print("_ ",end="")
#             print(items,end=" ")
 
#         print(" ")
   
# while True:
#     linha = int(input("Qual a linha: "))
#     coluna = int(input("Qual a coluna: "))
#     caracter = input("Qual o caracter: ")
#     jogue_o_jogo(mesa,linha, coluna, caracter)
#     contador += 1
#     if contador == 9:
#         exibe_resultado()
#         break

# # Resolução GPT
# # Cria o tabuleiro vazio
# velha = [[" " for _ in range(3)] for _ in range(3)]

# # Função para imprimir o tabuleiro
# def imprimir_tabuleiro(tabuleiro):
#     for linha in tabuleiro:
#         print("|".join(linha))
#         print("-" * 5)

# # Função para verificar vitória
# def verificar_vitoria(tabuleiro, jogador):
#     for i in range(3):
#         # Verifica linhas e colunas
#         if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
#             return True
#         if tabuleiro[0][i] == jogador and tabuleiro[1][i] == jogador and tabuleiro[2][i] == jogador:
#             return True
#     # Verifica diagonais
#     if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
#         return True
#     if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
#         return True
#     return False

# # Função principal do jogo
# def jogue_o_jogo():
#     jogadores = ['O', 'X']
#     jogadas = 0

#     while jogadas < 9:
#         imprimir_tabuleiro(velha)
#         jogador = jogadores[jogadas % 2]
#         print(f"Vez do jogador '{jogador}'")

#         linha = int(input("Digite a linha (0, 1 ou 2): "))
#         coluna = int(input("Digite a coluna (0, 1 ou 2): "))

#         # Verifica se a entrada é válida
#         if linha >= 0 and linha <= 2 and coluna >= 0 and coluna <= 2:
#             if velha[linha][coluna] == " ":
#                 velha[linha][coluna] = jogador
#                 jogadas += 1

#                 if verificar_vitoria(velha, jogador):
#                     imprimir_tabuleiro(velha)
#                     print(f"Jogador '{jogador}' venceu!")
#                     return
#             else:
#                 print("Essa posição já está ocupada!")
#         else:
#             print("Posição inválida! Use valores entre 0 e 2.")

#     imprimir_tabuleiro(velha)
#     print("Empate!")

# # Executa o jogo
# jogue_o_jogo()

# Resolução do Claude
# PASSO 1: Criar o tabuleiro inicial
# Uma matriz 3x3 com espaços vazios representando as posições livres
tabuleiro = [
    [' ', ' ', ' '],  # Linha 0
    [' ', ' ', ' '],  # Linha 1
    [' ', ' ', ' ']   # Linha 2
]

# PASSO 2: Função para mostrar o tabuleiro na tela
def mostrar_tabuleiro():
    print("\nTabuleiro:")
    # Loop para percorrer as 3 linhas do tabuleiro
    for i in range(3):
        # Mostra cada linha com os símbolos separados por |
        print(f" {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} ")
        # Se não for a última linha, desenha a linha separadora
        if i < 2:
            print("---|---|---")

# PASSO 3: Função para verificar se alguém ganhou
def verificar_ganhador():
    # Verificar linhas e colunas
    for i in range(3):
        # Verifica se uma linha inteira tem o mesmo símbolo (e não está vazia)
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]  # Retorna o símbolo do ganhador
        
        # Verifica se uma coluna inteira tem o mesmo símbolo (e não está vazia)
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]  # Retorna o símbolo do ganhador
    
    # Verificar diagonal principal (canto superior esquerdo ao inferior direito)
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]  # Retorna o símbolo do ganhador
    
    # Verificar diagonal secundária (canto superior direito ao inferior esquerdo)
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]  # Retorna o símbolo do ganhador
    
    # Se ninguém ganhou, retorna None
    return None

# PASSO 4: Configuração inicial do jogo
jogador = 'X'  # Jogador X sempre começa
jogadas = 0    # Contador de jogadas (máximo 9 no jogo da velha)

# PASSO 5: Mostrar as instruções para o usuário
print("JOGO DA VELHA")
print("Digite linha e coluna (0, 1 ou 2)")

# PASSO 6: Loop principal do jogo
# Continua até que se façam 9 jogadas (tabuleiro cheio) ou alguém ganhe
while jogadas < 9:
    # Mostra o estado atual do tabuleiro
    mostrar_tabuleiro()
    
    # PASSO 7: Pedir a jogada do usuário
    print(f"\nVez do jogador {jogador}")
    linha = int(input("Linha: "))    # Pede a linha (0, 1 ou 2)
    coluna = int(input("Coluna: "))  # Pede a coluna (0, 1 ou 2)
    
    # PASSO 8: Verificar se a posição escolhida está livre
    if tabuleiro[linha][coluna] == ' ':
        # Posição livre: fazer a jogada
        tabuleiro[linha][coluna] = jogador  # Coloca o símbolo do jogador
        jogadas += 1  # Incrementa o contador de jogadas
        
        # PASSO 9: Verificar se o jogador atual ganhou
        ganhador = verificar_ganhador()
        if ganhador:
            # Se alguém ganhou, mostra o tabuleiro final e anuncia o vencedor
            mostrar_tabuleiro()
            print(f"\nJogador {ganhador} GANHOU!")
            break  # Sai do loop e termina o jogo
        
        # PASSO 10: Trocar de jogador para a próxima rodada
        # Se era X, vira O. Se era O, vira X
        jogador = 'O' if jogador == 'X' else 'X'
    else:
        # Posição ocupada: avisar o usuário e pedir nova jogada
        print("Posição ocupada! Tente outra.")

# PASSO 11: Verificar empate
# Se saiu do loop por limite de jogadas (9) e ninguém ganhou, é empate
if not verificar_ganhador():
    mostrar_tabuleiro()
    print("\nEMPATE!")