def triangulo(x):
    contador = 0
    while contador < x:
        elementos = "#" * (contador + 1)
        print(elementos)
        contador += 1
        
triangulo(5)