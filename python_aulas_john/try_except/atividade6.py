# # Dicionário de exemplo
# dados = {"nome": "João", "idade": 30}

# try:
#     # Operação que pode gerar TypeError
#     resultado = 10 + "5"  # Somar número com string (TypeError)
    
#     # Operação que pode gerar KeyError
#     cidade = dados["cidade"]  # Acessar chave inexistente (KeyError)
    
#     # Operação que pode gerar RuntimeError
#     if len(dados) > 5:
#         raise RuntimeError("Muitos dados!")  # Forçar RuntimeError

# except TypeError:
#     print("Erro: Tipo de dado inválido (você tentou operações com tipos incompatíveis)")

# except KeyError:
#     print("Erro: Chave não encontrada no dicionário")

# except RuntimeError:
#     print("Erro: Problema durante a execução do programa")

# else:
#     print("Tudo funcionou perfeitamente!")
    
# finally:
#     print("Fim do programa")
    
try:
    # 1. TypeError: tentando somar número com string
    resultado = 10 + "dez"
        
    # 2. KeyError: acessando uma chave inexistente em um dicionário
    dados = {"nome": "Ariel", "idade": 18}
    print(dados["altura"])
        
    # 3. RuntimeError: gerado manualmente para exemplo
    raise RuntimeError("Erro em tempo de execução!")
    
except TypeError:
    print("TypeError: Você tentou realizar uma operação com tipos incompatíveis (ex: int + str).")
    
except KeyError:
    print("KeyError: A chave acessada não existe no dicionário.")
    
except RuntimeError as e:
    print(f"RuntimeError: {e}")