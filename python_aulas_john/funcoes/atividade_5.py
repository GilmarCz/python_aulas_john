# def quadradoString(string, numero):
#     linha = 0
#     while linha < numero:
#         # Cria a linha rotacionada
#         linhas = string[linha:] + string[:linha]
#         print(linhas)
#         linha += 1

# # Exemplo de uso (sem inputs, usando os parâmetros diretamente):
# quadradoString("abcde", 6)

# def quadradoString():
#     texto = input("Digite algo: ") # Exemplo: "abc" (índices 0:a, 1:b, 2:c)
#     tamanho = int(input("Digite tamanho: ")) # Tamanho = 3 (0,1,2)
#     indice = 0 # Começa no índice 0
    
#     while indice < tamanho: # Loop enquanto 0<3 | 1<3 | 2<3 | 3<3 (falso para o laço para aqui)
#         print(texto[indice:] + texto[:indice]) # Concatena partes da string
#         indice += 1 # Incrementa o índice: 0→1→2→3
        
# quadradoString() # Chama a função para executa-lá
        
# """     Iteração	indice	texto[indice:]	texto[:indice]	Saída
#         1ª	        0	    "abc"	        "" (vazio)	    "abc" + "" = "abc"
#         2ª	        1	    "bc"	        "a"	            "bc" + "a" = "bca"
#         3ª	        2	    "c"	            "ab"	        "c" + "ab" = "cab" """

# Define a função quadradoString que não recebe parâmetros
# def quadradoString():
#     # Pede ao usuário para digitar uma string e armazena em 'texto'
#     texto = input("Digite algo: ")  # Exemplo: se usuário digitar "abc", texto = "abc"
    
#     # Calcula o comprimento da string e armazena em 'tamanho'
#     tamanho = int(input("Digite tamanho: "))  # Para "abc", tamanho = 3
    
#     # Inicializa a variável 'linha' que controlará qual rotação estamos construindo
#     linha = 0  # Começamos pela primeira rotação (linha 0)
    
#     # Loop principal: executa enquanto não processarmos todas as rotações
#     while linha < tamanho:  # Para "abc": 0<3, 1<3, 2<3, 3<3 (para)
#         # Inicializa uma string vazia para construir a linha rotacionada
#         resultado = ""  # Aqui vamos montar cada linha do quadrado
        
#         # Define a posição inicial como o número da linha atual
#         pos = linha  # Na primeira iteração pos=0, depois 1, depois 2
        
#         # Inicializa contador para controlar quantos caracteres já adicionamos
#         contador = 0  # Vai de 0 até tamanho-1
        
#         # Loop interno: constrói a string rotacionada caractere por caractere
#         while contador < tamanho:  # Para "abc": precisa adicionar 3 caracteres
#             # Se a posição atual ultrapassar o fim da string
#             if pos >= tamanho:  # Ex: se tamanho=3 e pos=3
#                 pos = 0  # Volta para o início da string (rotaciona)
            
#             # Adiciona o caractere na posição atual ao resultado
#             resultado += texto[pos]  # Para "abc", linha 1: pos 1="b", depois 2="c", depois 0="a"
            
#             # Move para a próxima posição na string
#             pos += 1  # Incrementa a posição
            
#             # Incrementa o contador de caracteres adicionados
#             contador += 1  # Controla quando terminamos de montar a linha
        
#         # Imprime a linha rotacionada completa
#         print(resultado)  # Ex: para "abc" na linha 1 imprime "bca"
        
#         # Avança para a próxima linha/rotação
#         linha += 1  # Incrementa o contador de linhas

# # Chama a função para executá-la
# quadradoString()  # Isso inicia todo o processo

def Repetir(palavra, numero):
    stringTotal = (palavra * numero)
    linha = 0
    while linha < numero:
        coluna = 0
        letras = " "
        while coluna < numero:
            posição = linha*numero + coluna
            letras += stringTotal[posição]
            coluna += 1
        print(letras)
        linha += 1
Repetir("Jumanji", 4)