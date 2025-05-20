def printa_varias_vezes(texto, vezes):
    return (texto + "\n") * vezes

# Chamada correta com argumentos
texto = input("Seu texto: ")
vezes = int(input("Quantas vezes repetir: "))
print(printa_varias_vezes(texto, vezes))