# palavra1 ="ex"
# palavra2 ="emplo"
# palavra = palavra1+palavra2
# print(palavra * 5)
# print("2" * len(palavra))

# p1 = input("Digite uma palavra: ")
# p2 = input("Digite outra palavra: ")

# if len(p1) > len(p2):
#     print(p1)
# elif len(p1) == len(p2):
#     print("tamahos iguais")
# else:
#     print(p2)

# entrada = input("Digite um texto: ")
# # print(entrada[0])
# # print(entrada[1])
# # print(entrada[2])
# ultimo = len(entrada) - 1
# print(f"O ultimo caracter da palavra {entrada} é {entrada[ultimo]}")

# string_entrada = input("Por favor, digite uma string: ") # Solicita ao usuário para digitar uma string
# print(string_entrada[0]) # Imprime o primeiro caractere da string
# print(string_entrada[1]) # Imprime o segunda caractere da string
# print(string_entrada[3]) # Imprime o quarta caractere da string

# entrada = input("Por favor, digite uma string: ")
# penultimo = len(entrada)
# if entrada[1] == entrada[penultimo - 2]:
#     print(f"O segundo caracter e o penultimo são iguais {entrada[1]} = {entrada[penultimo - 2]}")
# else:
#     print("Tente outra vez!!!")
    

# def quadradoString(string, numero):
#     linha = 0
#     while linha < numero:
#         # Cria a linha rotacionada
#         linhas = string[linha:] + string[:linha]
#         print(linhas)
#         linha += 1

# # Exemplo de uso (sem inputs, usando os parâmetros diretamente):
# quadradoString("abcde", 5)

# def quadradoString():
#     texto = input("Digite algo: ") # Exemplo: "abc" (índices 0:a, 1:b, 2:c)
#     tamanho = len(texto) # Tamanho = 3 (0,1,2)
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
def quadradoString():
    # Pede ao usuário para digitar uma string e armazena em 'texto'
    texto = input("Digite algo: ")  # Exemplo: se usuário digitar "abc", texto = "abc"
    
    # Calcula o comprimento da string e armazena em 'tamanho'
    tamanho = len(texto)  # Para "abc", tamanho = 3
    
    # Inicializa a variável 'linha' que controlará qual rotação estamos construindo
    linha = 0  # Começamos pela primeira rotação (linha 0)
    
    # Loop principal: executa enquanto não processarmos todas as rotações
    while linha < tamanho:  # Para "abc": 0<3, 1<3, 2<3, 3<3 (para)
        # Inicializa uma string vazia para construir a linha rotacionada
        resultado = ""  # Aqui vamos montar cada linha do quadrado
        
        # Define a posição inicial como o número da linha atual
        pos = linha  # Na primeira iteração pos=0, depois 1, depois 2
        
        # Inicializa contador para controlar quantos caracteres já adicionamos
        contador = 0  # Vai de 0 até tamanho-1
        
        # Loop interno: constrói a string rotacionada caractere por caractere
        while contador < tamanho:  # Para "abc": precisa adicionar 3 caracteres
            # Se a posição atual ultrapassar o fim da string
            if pos >= tamanho:  # Ex: se tamanho=3 e pos=3
                pos = 0  # Volta para o início da string (rotaciona)
            
            # Adiciona o caractere na posição atual ao resultado
            resultado += texto[pos]  # Para "abc", linha 1: pos 1="b", depois 2="c", depois 0="a"
            
            # Move para a próxima posição na string
            pos += 1  # Incrementa a posição
            
            # Incrementa o contador de caracteres adicionados
            contador += 1  # Controla quando terminamos de montar a linha
        
        # Imprime a linha rotacionada completa
        print(resultado)  # Ex: para "abc" na linha 1 imprime "bca"
        
        # Avança para a próxima linha/rotação
        linha += 1  # Incrementa o contador de linhas

# Chama a função para executá-la
quadradoString()  # Isso inicia todo o processo