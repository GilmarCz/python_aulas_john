def lista_produtos():
    lista =["arroz","feijão","açucar","café","macarrão"]
    while True:
        nome = input("Digite um produto e caso queira sair digite 'sair' : ")
        if nome in lista:
            print(f"O produto: {nome} esta na lista!")
        elif nome == "sair":
            break
        else:
           print(f"O produto: {nome} não esta na lista!") 
           
lista_produtos()
    