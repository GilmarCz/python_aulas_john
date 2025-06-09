import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")

# Head() lê as cinco primeiras linhas | Tail() lê as cinco ultimas linhas
print("Primeiras 5 linhas do DataFrame")
print(df_filmes.head())
print("Ultimas 5 linhas do DataFrame")
print(df_filmes.tail())

# Info
print("\nInformações sobre o DataFrame")
print(df_filmes.info())

# Shape - dimensões
print(f"\nO dataFrame de filmes tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}") 

# Describe
# Gera estatistica do DataFrame
print("Estatisca descritiva do DataFrame:")
print(df_filmes.describe())

# Index 
# Traz informações sobre os índices das linhas
print("Informações do índice")
print(df_filmes.index)
