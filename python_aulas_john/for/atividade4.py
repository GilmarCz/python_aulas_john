numeros = [1, 0, 2, 4, 5, 7, 10]

def numeros_pares(lista: list):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

print(numeros_pares(numeros))  # Saída: [0, 2, 4, 10]
