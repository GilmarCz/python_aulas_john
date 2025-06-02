# Try e Except: Tratar erros
# try:
#     numero = int(input("Digite um número: "))
#     print(f"Você digitou: {numero} ")
# except ValueError:
#     print("Erro!!! Digite um número!")
    
# numero1 = int(input("Digite um número: "))
# print(f"Você digitou: {numero1} ")

try:
    num_str = input("Digite um número: ")
    num_int = int(num_str)
    resultado = 10 / num_int
    print(f"10 dividido por {num_int} é {resultado}")
except ValueError:
    print("Erro!!! Entrada inválida! Por favor, digite um número")
    
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero")
    
except Exception as e:
    print("Ocorreu um erro inesperado {e}")

# Else só vai ser executado se não houver nenhuma exceção    
else:
    print("OK, deu certo!")
 
# Executa mesmo que tenha erro ou não no try   
finally:
    #num_str = input("Digite um número: ")
    if num_int == 0:
        num_int = int(input("Digite um número: "))