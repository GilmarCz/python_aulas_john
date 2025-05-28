palavra = "Minha palavra"
def sem_vogal(string1):
    print(palavra)
    nova_palavra = string1
    for i in "aeiou":
        nova_palavra = nova_palavra.replace(i,"")
    return nova_palavra
print(sem_vogal(palavra))