# Atividade 11
capital_inicial = float(input("Digite seu capital inicial (R$): "))
tx_juros = float(input("Digite a taxa de juros anual (%): "))
anos = float(input("Quantos anos? "))
juros = float(tx_juros / 100) 
juros_simples = float(capital_inicial * juros * anos)
montante = capital_inicial + juros_simples
print(f"Seu montante final será de: R$ {montante:.2f}")
