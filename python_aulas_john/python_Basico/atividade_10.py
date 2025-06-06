# Atividade 10
valor = float(input("Digite o valor a converter: R$ "))
dolar = float(5.99)
conversao = float(valor/dolar)
print(f"Voce tem US${conversao:.2f} dolares")
print(f"\nValor convertido:")
print(f"R$ {valor:.2f} → US$ {conversao:.2f} (Taxa: 1 USD = {dolar} BRL)")
