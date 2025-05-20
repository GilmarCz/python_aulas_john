# Atividade 8
preco = float(input("Qual o preço do produto? R$"))
desconto = float(input("Qual o desconto do produto? (%) "))
valor = preco - preco*(desconto/100)
print(f"O valor com desconto é R${valor:.2f}")