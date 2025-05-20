texto = input("Digite algo: ")
tamanho = len(texto)
if tamanho < 20:
    # Completa com asteriscos no início
    texto_formatado = "*" * (20 - tamanho) + texto
else:
    texto_formatado = texto[:20]  # Corta se for maior que 20 caracteres

print(texto_formatado)