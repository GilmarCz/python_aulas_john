# Atividade 24
tempAmanha = int(input("Qual a previsão do tempo para amanhã? Temperatura: "))
chuva = input("Vai chover? (sim / não)")
if tempAmanha > 20 and chuva == "não":
    print("Use jeans e camiseta")
elif tempAmanha > 20 and chuva == "sim":
    print("Use jeans, camiseta e guarda-chuva!!!")
elif tempAmanha > 10 and tempAmanha <= 20 and chuva == "não":
    print("Use jeans, camiseta e agasalho")
elif tempAmanha > 10 and tempAmanha <= 20 and chuva == "sim":
    print("Use jeans, camiseta, agasalho e guarda-chuva!!!")
elif tempAmanha > 5 and tempAmanha <= 10 and chuva == "não":
    print("Use jeans, camiseta e japona!!!")
elif tempAmanha > 5 and tempAmanha <= 10 and chuva == "sim":
    print("Use jeans, camiseta, japona e guarda-chuva!!!")
elif tempAmanha <= 5 and chuva == "não":
    print("Agasalhe-se bem tá FRIO!!!")
elif tempAmanha <= 5 and chuva == "sim":
    print("Agasalhe-se bem tá FRIO!!! Pegue o guarda-chuva!!!")
else:
    print("Resposta inválida sobre a chuva. Digite 'sim' ou 'não'.")

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