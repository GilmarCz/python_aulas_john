# Solicita ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo que deseja abrir: ")

try:
    # Tenta abrir o arquivo no modo leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Se conseguir abrir, mostra mensagem de sucesso
        print(f"Arquivo '{nome_arquivo}' aberto com sucesso!")
        # Aqui você pode adicionar o processamento do arquivo
        
except FileNotFoundError:
    # Caso o arquivo não exista, mostra mensagem personalizada
    print("Arquivo não encontrado.")
except Exception as e:
    # Captura outros erros que podem ocorrer (como permissão)
    print(f"Ocorreu um erro ao tentar abrir o arquivo: {str(e)}")
    
    
# Solicita ao usuário o nome do arquivo
nome_arquivo1 = input("Digite o nome do arquivo que deseja abrir: ")

try:
    # Abre o arquivo no modo leitura (sem usar 'with')
    arquivo1 = open(nome_arquivo1, 'r')
    
    # Se conseguir abrir, mostra mensagem de sucesso
    print(f"Arquivo '{nome_arquivo1}' aberto com sucesso!")
    
    # Aqui você pode processar o arquivo...
    # Exemplo: ler e mostrar o conteúdo
    conteudo = arquivo1.read()
    print("\nConteúdo do arquivo:")
    print(conteudo)
    
    # Fecha o arquivo manualmente
    arquivo1.close()
    
except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Sem permissão para acessar o arquivo.")
except IOError as e:
    print(f"Erro de E/S ao abrir o arquivo: {str(e)}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {str(e)}")
finally:
    # Garante que o arquivo será fechado mesmo se ocorrer um erro
    if 'arquivo' in locals() and not arquivo1.closed:
        arquivo1.close()