# Função com print dentro dela para exibir o resultado da execução
def soma():
    print (5 + 5)
    
soma()

# Função com retorno(O Return não imprime nada, é só retorna da execução)
def soma2():
    soma = 5+5
    return soma # esse é o tipo mais usado

print( soma2() + 5)

#-----------------------------Prática-----------------------------------------
def sete_irmaos():
    irmaos = ["José", "Beto", "Antônio","Zeca", "Maria", "Helena", "Ana"]
    irmaos.sort()
    return irmaos
print(sete_irmaos()) # o que está dentro do print é um ARGUMENTO

def soma3(x,y): # o que está dentro dos parenteses da função, são PARÂMETROS
    return x+y
print(soma3(200, 10))
print(soma3(50, 60))
print(soma3(2, 8))