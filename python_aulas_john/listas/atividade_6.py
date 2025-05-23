def duplicados():
    numeros = []
    while len(numeros) < 10:
        nun = int(input(f"Digite o {len(numeros)+1}º número: "))
        numeros.append(nun)
    unicos = []
    repetidos = []
    i = 0
    while i < len(numeros):
            if numeros[i] not in unicos:
                unicos.append(numeros[i])
            else:
                repetidos.append(numeros[i])
            i += 1
    print("Todos os números digitados:", numeros)
    print("Números únicos (sem repetição):", unicos)
    print("Números repetidos:", repetidos)
duplicados()