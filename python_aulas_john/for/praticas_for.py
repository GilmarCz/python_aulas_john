# digita = input("Digite algo: ")
# for caracter in digita:
#     #print(caracter + "*")
#     print(caracter,end="*")

# num = int(input("Digite um número inteiro positivo: "))
# for i in range(-num,num+1):
#     if i != 0:        
#         print(i)
#         #print(i,end=" ")

# minha_string = "Uma obra de Carolina Maria de Jesus, que relata a vida de uma favelada"

# def mais_caracteres(string1):
#     print(string1)
#     string1 = string1.replace(" ", "")  # Remove os espaços
#     mais_frequente = ""  # Inicia uma variável com uma string vazia
#     max_contagem = 0  # Variável inicializada em 0 para guardar a maior contagem

#     for caractere in string1:  # Percorre a string caractere por caractere
#         contagem = string1.count(caractere)  # Conta quantas vezes o caractere aparece na string
#         if contagem > max_contagem:  # Se a contagem for maior que o valor atual de max_contagem
#             max_contagem = contagem  # Atualiza max_contagem com o novo valor
#             mais_frequente = caractere  # Armazena o caractere mais frequente até o momento

#     return f"Caractere mais frequente: '{mais_frequente}' apareceu {max_contagem} vezes"

# print(mais_caracteres(minha_string))

#minha tentativa de resolução
""" lista_bidimensional = [[0,1,2,3],[0,8,6,9],[1,2,7,4],[4,5,6,8]]
num = 1
def conta_elementos_mach(minha_matriz: list, elemento: int):
    for i in minha_matriz.count(num):
        return minha_matriz

print(conta_elementos_mach(lista_bidimensional,num)) """

# lista_bidimensional = [[0,1,2,3],[0,8,6,9],[1,2,7,4],[4,5,6,8]]
# num = 4
# def conta_elementos_mach(minha_matriz: list, elemento: int):
#     contagem = 0
#     for linha in minha_matriz:
#         contagem += linha.count(elemento)  # Conta quantas vezes o elemento aparece em cada linha
#     return contagem

# print(conta_elementos_mach(lista_bidimensional,num))

# resolução John
lista_bidimensional = [[0,1,2,3],[0,8,6,9],[1,2,7,4],[4,5,6,8]]
num = 4
def conta_elementos_mach(minha_matriz: list, elemento: int):
    contagem = 0
    for linha in minha_matriz:
        for item in linha:
            if item == elemento:
                contagem += 1
    return contagem

print(conta_elementos_mach(lista_bidimensional,num))