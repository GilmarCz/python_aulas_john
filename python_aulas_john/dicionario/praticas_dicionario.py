# Primeira tentativa
# def histogram(palavra: str):
#     p1 = {}
#     for letra in palavra:
#         if letra not in p1:
#             p1[letra] = 0
#         p1[letra] += 1
#     return (p1 * "*")
# print(histogram("abba"))

def histogram(palavra: str):
    p1 = {}
    for letra in palavra:
        if letra not in p1:
            p1[letra] = 0
        p1[letra] += 1
    resultado = ""  # String para armazenar o histograma formatado
    for letra in p1:
        resultado += f"{letra}: {'*' * p1[letra]}\n"  # Concatena a letra e seus asteriscos

    return resultado
print(histogram("papagaio"))