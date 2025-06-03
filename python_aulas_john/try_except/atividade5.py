try:
    lista = [10, 45, 98]
    i = len(lista)
    num1 = int(input("Digite um número divisor: "))
    num2 = int(input(f"Digite um índice de 0 a {i-1}: "))
    resultado = lista[num2] / num1
    print(f"A divisão de {lista[num2]} por {num1} é {resultado}")
    
except ValueError:
    print("Erro!!! Entrada inválida! Por favor, digite um número válido.")
    
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
    
except IndexError:
    print(f"Erro: Índice inválido! Digite um valor entre 0 e {i-1}.")
    
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

else:
    print("Operação realizada com sucesso!")
    
finally:
    print("Fim da execução do programa.")