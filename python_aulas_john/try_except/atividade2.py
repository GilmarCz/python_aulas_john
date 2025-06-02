try:
    num_str1 = input("Digite um número: ")
    num_str2 = input("Digite outro número: ")
    num_int1 = int(num_str1)
    num_int2 = int(num_str2)
    resultado = num_int1 / num_int2
    print(f"A divisão de {num_int1} por {num_int2} é {resultado}")
except ValueError:
    print("Erro!!! Entrada inválida! Por favor, digite um número")
    
except ZeroDivisionError:
    print("Erro: Não é possivel dividir por zero")
    
except Exception as e:
    print("Ocorreu um erro inesperado {e}")

# Else só vai ser executado se não houver nenhuma exceção    
else:
    print("OK, deu certo!")