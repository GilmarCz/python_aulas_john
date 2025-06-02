arquivo = None

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
    print("Arquivo lido com sucesso")
    
except FileNotFoundError:
    print("Erro: Arquivo não encontrado")

except Exception as e:
    print("Erro ao ler o arquivo: {e}")
    
else:
    print("Processamento do arquivo concluido com sucesso")
    
finally:
    if arquivo:
        arquivo.close()
        print("Arquivo fechado")