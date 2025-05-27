lista_numeros = [3, 7, 1, 1, 2]
def lista_estrelas(lista: list):    
    for i in lista:
        estrela = "*" * i
        print(estrela)
lista_estrelas(lista_numeros)