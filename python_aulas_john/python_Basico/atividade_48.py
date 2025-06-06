# Atividade 48
sup = int(input("Digite um limite superior: "))
multi= int(input("Qual é o multiplicador (maior igual a 2): "))
i = 1
while i <= sup:
    print(i)
    i *= multi
print(f"O limite era: {sup}")