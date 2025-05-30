def invert(dicionario: dict):
    # Cria um dicionário vazio para armazenar o resultado invertido
    invertido = {}
    
    # Percorre cada par chave-valor do dicionário recebido
    for chave, valor in dicionario.items():  # .items() permite acessar chave e valor
        # Inverte: valor vira chave, chave vira valor
        invertido[valor] = chave
    
    # Retorna o dicionário invertido
    return invertido

# Cria um dicionário com dados de uma pessoa
Pessoa = {"nome": "Ariel", "altura": 150, "peso": 70, "idade": 18}

# Exibe o dicionário original
print("Dicionário original:")
print(Pessoa)

# Chama a função para inverter e armazena o resultado em uma variável
invertido = invert(Pessoa)

# Exibe o dicionário invertido
print("Dicionário invertido:")
print(invertido)
