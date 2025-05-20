# Atividade 16
# numero = int(input("Digite um número: "))
# if numero < 0:
#     numero *= -1
#     print(numero)
# else:
#     print(numero)
# PS C:\Users\gilmar.2970\Documents\GitHub\aula-python> & C:/Users/gilmar.2970/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/gilmar.2970/Documents/GitHub/aula-python/projeto python/atividades_condicional.py"
# Digite um número: 8
# 8
# PS C:\Users\gilmar.2970\Documents\GitHub\aula-python> & C:/Users/gilmar.2970/AppData/Local/Microsoft/WindowsApps/python3.13.exe "c:/Users/gilmar.2970/Documents/GitHub/aula-python/projeto python/atividades_condicional.py"
# Digite um número: -5
# 5

# Atividade 17
# nome = input("Digite um nome: ")
# if nome != "Jerry":
#     porcao = int(input("Quantas poorções? "))
#     preco = 5.9
#     conta = porcao * preco
#     print(f"Sua conta é {conta}")
# else:
#     print(f"Acertou misseravel!!!")    

# nome = input("Digite um nome: ")
# if nome == "Jerry":
#     porcao = int(input("Quantas porções? "))
#     preco = 5.9
#     conta = porcao * preco
#     print(f"Sua conta é {conta}")
# else:
#     print(f"Errou misseravel!!!")    

# Atividade 18
# numero = int(input("Digite um número inteiro: "))
# if numero > 100 and numero < 1000:
#     print(f"Este número ({numero}) está entre 100 e 1000. Obrigado!")
# elif numero <= 100 and numero > 10:
#     print(f"Este número ({numero}) é menor ou igual a 100 e maior que 10. Obrigado!")
# elif numero <= 10:
#     print(f"Este número ({numero}) é menor ou igual a 10. Obrigado!")
# else:
#     print(f"Este número ({numero}) é maior ou igual a 1000. Obrigado!")

# Atividade 19
# nome = "Gilmar"
# cidade = "Curitiba"
# estado = "Paraná"
# cep = "81000-000"
# dig_nome = input("Digite um nome: ")

# if nome == dig_nome:
#     print(f"nome: {dig_nome}, \ncidade: {cidade}, \nestado: {estado}, \nCEP: {cep}.")
# else:
#     print("Esse usuário não existe no nosso BD")

# Atividade 20
# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))
# operacao = input(" Digite uma operação matematica(adição, subtração, multiplicação ou divisão): ")
# if operacao == "adição":
#     calculo = n1 + n2
#     print(f"O resultado de {n1}+{n2} é: {calculo}")
# elif operacao == "subtração":
#     calculo = n1 - n2
#     print(f"O resultado de {n1}-{n2} é: {calculo}")
# elif operacao == "multiplicação":
#     calculo = n1 * n2
#     print(f"O resultado de {n1}x{n2} é: {calculo}")
# elif operacao == "divisão":
#     calculo = n1 / n2
#     print(f"O resultado de {n1}/{n2} é: {calculo}")
# else:
#     print("_______")
    
# Atividade 21
# fahrenheit = float(input("Digite a temperatura em Fahrenheit (°F): "))
# celsius = (fahrenheit - 32) / 1.8 
# print(f"{fahrenheit}°F = {celsius:.1f}°C")
# if celsius < 0:
#     print(f"Brr!!! Está frio aqui!")
# Digite a temperatura em Fahrenheit (°F): 132
# 132.0°F = 55.6°C
# Digite a temperatura em Fahrenheit (°F): 25
# 25.0°F = -3.9°C
# Brr!!! Está frio aqui!

# Atividade 22
# salHora = float(input("Qual seu salario/hora? "))
# horas = float(input("Quantas horas você trabalha? "))
# semana = input("Qual o dia da semana você trabalha? ")
# if semana == "domingo" or semana == "Domingo":
#     salario = salHora * horas * 2
# else:
#     salario = salHora * horas    
# print(f"Salário diario é R$ {salario:.2f}")

# Atividade 23
# pontos = float(input("Pontos do cliente: "))
# if pontos < 100:
#     bonus = "10%"
# else:
#     bonus = "15%"    
# print(bonus)

# Atividade 24
# tempAmanha = int(input("Qual a previsão do tempo para amanhã? Temperatura: "))
# chuva = input("Vai chover? (sim / não)")
# if tempAmanha > 20 and chuva == "não":
#     print("Use jeans e camiseta")
# elif tempAmanha > 20 and chuva == "sim":
#     print("Use jeans, camiseta e guarda-chuva!!!")
# elif tempAmanha > 10 and tempAmanha <= 20 and chuva == "não":
#     print("Use jeans, camiseta e agasalho")
# elif tempAmanha > 10 and tempAmanha <= 20 and chuva == "sim":
#     print("Use jeans, camiseta, agasalho e guarda-chuva!!!")
# elif tempAmanha > 5 and tempAmanha <= 10 and chuva == "não":
#     print("Use jeans, camiseta e japona!!!")
# elif tempAmanha > 5 and tempAmanha <= 10 and chuva == "sim":
#     print("Use jeans, camiseta, japona e guarda-chuva!!!")
# elif tempAmanha <= 5 and chuva == "não":
#     print("Agasalhe-se bem tá FRIO!!!")
# elif tempAmanha <= 5 and chuva == "sim":
#     print("Agasalhe-se bem tá FRIO!!! Pegue o guarda-chuva!!!")
# else:
#     print("Resposta inválida sobre a chuva. Digite 'sim' ou 'não'.")

# graus = int(input("Digite a temperatura: "))
# chuva = int(input("Var chover? 0 - Não, 1 - Sim: "))
# if graus > 20:
#     if chuva == 0:
#         print("Use jeans e camiseta")
#     else:
#         print("Use jeans e camiseta mas leve um Guarda Chuva")    
# elif graus >= 10 and graus < 20:
#     if chuva == 0:
#         print("Use jeans e camiseta e leve um suéter")
#     else:
#         print("Use jeans e camiseta e leve um suéter. Leve Guarda-Chuva")        
# elif graus >= 5 and graus < 10:
#     if chuva == 0:
#         print("Eta Pega!! Frio da peste! Não saia de casa")
#     else:
#         print("Não saia! Frio do Djanho e Muita chuva")
# else:
#     print("Nem pense! Durma")

# Atividade 25
# idade = int(input("Sua idade? "))
# if idade >= 18:
#     print("É de MAIOR!!!")
# else:
#     print("DI MENOR !!!")

# Atividade 26
# n1 = float(input("Nota 1: "))
# n2 = float(input("Nota 2: "))
# media = (n1 + n2) / 2
# if media >= 7:
#     print("Aprovado!!")
# else:
#     print("Reprovado!!!")

# Atividade 27
# preco = float(input("Preço: R$ "))
# if preco <= 50:
#     print("Categoria Econômica")
# elif preco > 50 and preco <= 100:
#     print("Categoria Intermediária")
# else:
#     print("Categoria Premium")

# Atividade 28
# idade = int(input("Sua idade? "))
# if idade >= 16:
#     print("Pode votar!")
# else:
#     print("Não pode votar")

# Atividade 29
# mes = int(input("Digite um mês: "))
# if mes == 1:
#     print("Janeiro")
# elif mes == 2:
#     print("Fevereiro")
# elif mes == 3:
#     print("Março")
# elif mes == 4:
#     print("Abril")
# elif mes == 5:
#     print("Maio")
# elif mes == 6:
#     print("Junho")
# elif mes == 7:
#     print("Julho")
# elif mes == 8:
#     print("Agosto")
# elif mes == 9:
#     print("Setembro")
# elif mes == 10:
#     print("Outubro")
# elif mes == 11:
#     print("Novembro")
# elif mes == 12:
#     print("Dezembro")
# else:
#     print("Mês Invalido")

# Atividade 30
# n1 = int(input("Digite um número"))
# n2 = int(input("Digite outro número"))
# if n1 > n2:
#     print(f"O maior número é: {n1}")
# elif n2 > n1:
#     print(f"O maior número é: {n2}")
# else:
#     print("Os números são iguais!")

# Atividade 31
# nome1 = input("1 Qual é seu nome? ")
# idade1 = int(input("1 Qual é sua idade? "))
# nome2 = input("2 Qual é seu nome? ")
# idade2 = int(input("2 Qual é sua idade? "))
# if idade1 > idade2:
#     print(f"O mais velho é {nome1} com {idade1} anos")
# else:
#     print(f"O mais velho é {nome2} com {idade2} anos")

# Atividade 32 repetido

# Atividade 33
# idade = int(input("Qual é sua idade? "))
# if idade >= 5:
#     print(f"Ok, você tem {idade} anos")
# elif idade < 5 and idade >= 0:
#     print(f"Suspeito que você não saiba escrever ...")
# else:
#     print(f"Isso deve ser um erro ...")

# Atividade 34
# nome = input("Nome? ")
# if nome == "Huguinho" or nome == "Zezinho" or nome == "Luizinho":
#     print("Você é sobrinho do Pato Donald?")
# elif nome == "Chiquinho" or nome == "Francisquinho":
#     print("Você é sobrinho do Mickey Mouse?")
# else:
#     print(f"Você é {nome}")