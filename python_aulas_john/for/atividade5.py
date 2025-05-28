listaA = [1,5,8]
listaB = [2,3,9]

def lista_soma(lista1,lista2):
    somaLista = []
    
    for i in range(len(listaA)):
        
        soma = listaA[i] + listaB[i]
        somaLista.append(soma)
        
    return somaLista

print(lista_soma(listaA,listaB))