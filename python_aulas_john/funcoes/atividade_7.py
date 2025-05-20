def linha(n, texto):     
    if texto == "":
        caractere = "*"
    else:
        caractere = texto[0]
    
    print(caractere * n)

def caixa_de_hashtag(altura):
    contador = 0
    while contador < altura:
        linha(10, "#")
        contador += 1
        
caixa_de_hashtag(7)
    