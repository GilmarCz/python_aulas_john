# Atividade 20
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = input(" Digite uma operação matematica(adição, subtração, multiplicação ou divisão): ")
if operacao == "adição":
    calculo = n1 + n2
    print(f"O resultado de {n1}+{n2} é: {calculo}")
elif operacao == "subtração":
    calculo = n1 - n2
    print(f"O resultado de {n1}-{n2} é: {calculo}")
elif operacao == "multiplicação":
    calculo = n1 * n2
    print(f"O resultado de {n1}x{n2} é: {calculo}")
elif operacao == "divisão":
    calculo = n1 / n2
    print(f"O resultado de {n1}/{n2} é: {calculo}")
else:
    print("_______")