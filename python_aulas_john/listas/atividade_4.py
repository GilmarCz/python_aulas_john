notas = []
aprovadas = [] 
while len(notas) < 5:
    nota = float(input("Digite as notas (0 - 10): "))
    notas.append(nota)    
    
    if nota >= 6 and nota <= 10:
        aprovadas.append(nota)    
    print(notas) 
        
print(f"Notas aprovadas: ",aprovadas)
   