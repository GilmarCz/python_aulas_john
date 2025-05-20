# Atividade 1
# nome = input("Qual seu nome? ")
# apelido = input("Qual seu apelido? ")
# endereco = input("Qual seu endereco? ")
# cidade_cep = input("Qual cidade e cep? ")
# print(f"{nome} {apelido} - {endereco} - {cidade_cep}")

# Atividade 2
# nomeh = input("Por favor digite um nome: ")
# anoh = input("Por favor digite um ano: ")
# print(f"{nomeh} é uma valente cavaleira, nascida no ano de {anoh}. Certa manhã, {nomeh} acordou com um barulho terrivel: um dragão se aproximava da aldeia. Somente {nomeh} poderia salvar os moradores da aldeia.")

# Atividade 3
# cidade = "São Paulo"
# print(cidade)
# cidade = "Rio de Janeiro"
# print(cidade)

# Atividade 4
# texto = "Texto" #string
# inteiro = 10 #int
# flutuante = 15.5 #float
# print(f"string:{texto}, inteiro:{inteiro}, float:{flutuante}")

# Atividade 5
# Definindo as partes da frase
# parte1 = "Python é uma linguagem"
# parte2 = " de programação poderosa!"
# print(parte1 + parte2)

# Atividade de Algoritimo
# salario = int(input("Qual seu salario?  "))
# horasMes = int(input("Quantas horas trabalhada no mês?  "))
# valorHora = salario/horasMes
# dia = 8
# porDia = valorHora * dia
# print (f"O funcionario ganha: R$ {valorHora} por hora.")
# print(f"Por dia ele ganha: R$ {porDia}.")
# n = "10"
# resultado = int(n) * 2
# print(resultado)

# Atividade 6
# n = int(input("Digite um número: "))
# triplo = n * 3
# print(f"3 vezes {n} é {triplo}")

# n1 = int(input("Digite um número: "))
# print(f"3 vezes {n1} é {n1 * 3}")

# Atividade 7
# nome = input("Qual o seu nome? ")
# ano = int(input("Em que ano você nasceu? "))
# idade = 2025 - ano
# print(f"Olá {nome}, você fará {idade} anos em 2025!")
# print(f"Olá {nome}, você fará {2025 - ano} anos em 2025!") # forma não usual, melhor fazer a operação em uma variavel externa

# Atividade 8
# preco = float(input("Qual o preço do produto? R$"))
# desconto = float(input("Qual o desconto do produto? (%) "))
# valor = preco - preco*(desconto/100)
# print(f"O valor com desconto é R${valor:.2f}")

# Atividade 9
# conta = float(input("A conta, é: R$"))
# gorjeta = float(input("Gorjeta de:(%) "))
# gorj = conta*(gorjeta/100)
# contaGorj = conta+gorj
# print(f"A sua conta ficou em R${contaGorj}")

# Atividade 10
# valor = float(input("Digite o valor a converter: R$ "))
# dolar = float(5.99)
# conversao = float(valor/dolar)
# print(f"Voce tem US${conversao:.2f} dolares")
# print(f"\nValor convertido:")
# print(f"R$ {valor:.2f} → US$ {conversao:.2f} (Taxa: 1 USD = {dolar} BRL)")

# Atividade 11
# capital_inicial = float(input("Digite seu capital inicial (R$): "))
# tx_juros = float(input("Digite a taxa de juros anual (%): "))
# anos = float(input("Quantos anos? "))
# juros = float(tx_juros / 100) 
# juros_simples = float(capital_inicial * juros * anos)
# montante = capital_inicial + juros_simples
# print(f"Seu montante final será de: R$ {montante:.2f}")

# Atividade 12
# dig1 = float(input("Digite o primeiro número: "))
# dig2 = float(input("Digite o segundo número: "))
# dig3 = float(input("Digite o terceiro número: "))
# media = (dig1 + dig2 + dig3)/3
# print(f"A média é: {media}")

# Atividade 13
# largura = float(input("Largura(cm): "))
# altura = float(input("Altura(cm): "))
# area = (largura * altura)
# perimetro = (2*(largura+altura))
# print(f"Area = {area} cm2 e Perimetro = {perimetro} cm")

# Atividade 14
celsius = float(input("Digite a temperatura em Celsius (°C): "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")