# Atividade 18
numero = int(input("Digite um número inteiro: "))
if numero > 100 and numero < 1000:
    print(f"Este número ({numero}) está entre 100 e 1000. Obrigado!")
elif numero <= 100 and numero > 10:
    print(f"Este número ({numero}) é menor ou igual a 100 e maior que 10. Obrigado!")
elif numero <= 10:
    print(f"Este número ({numero}) é menor ou igual a 10. Obrigado!")
else:
    print(f"Este número ({numero}) é maior ou igual a 1000. Obrigado!")
