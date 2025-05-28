palavra = "Minha palavra"
def sem_vogal(string1):
    print(palavra)
    nova_palavra = string1
    for i in "aeiou":
        nova_palavra = nova_palavra.replace(i,"")
    return nova_palavra
print(sem_vogal(palavra))

# Resolução John
# def sem_vogal(texto):
#     vogais ="aeiou"
#     nova_string = ""
    
#     for letra in texto:
#         if letra not in vogais:
#             nova_string += letra
#     return nova_string

# print(sem_vogal("banana"))