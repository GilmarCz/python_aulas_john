# Atividade 54
import re
while True:
    p1 = input("Digite a primeira palavra: ")
    p2 = input("Digite a segunda palavra: ")
    if len(p1) == len(p2):
        print("Ok, obrigado!!!")
        break
    else:
        p1 = input("Digite novamente a primeira palavra: ")
        p2 = input("Digite novamente a segunda palavra: ")
        