# def mesmo_caracter(texto, n1, n2):
#     # Verifica se os índices estão dentro dos limites
#     if n1 >= len(texto) or n2 >= len(texto) or n1 < 0 or n2 < 0:
#         return False
#     # Compara os caracteres
#     return texto[n1] == texto[n2]

# print(mesmo_caracter("arara", 1, 3))  # Retorna False

def mesmo_caracter(texto, n1, n2):
    # Verifica se os índices estão dentro dos limites
    if n1 >= len(texto) or n2 >= len(texto) or n1 < 0 or n2 < 0:
        return False
    else:
        if texto[n1] != texto[n2]:
            return False
        else:
            return True
print(mesmo_caracter("arara", 1, 10))