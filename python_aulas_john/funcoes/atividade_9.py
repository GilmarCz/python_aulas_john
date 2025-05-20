def o_maior_numero(x, y, z):
    maior = x
    if y > maior:
        maior = y
    if z > maior:
        maior = z
    return maior

o_maior_numero(50,15,90)

def o_maior_numero2(x, y, z):
    return max(x,y,z)

o_maior_numero2(25,40,89)