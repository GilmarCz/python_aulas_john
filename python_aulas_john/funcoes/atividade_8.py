def triangulo(x):
    contador = 0
    while contador < x:
        elementos = "#" * (contador + 1)
        print(elementos)
        contador += 1
        
triangulo(5)

def triangulo(x):
    contador = 0
    while contador < x:
        elementos = "#" * (x -contador)
        print(elementos)
        contador += 1
        
triangulo(5)