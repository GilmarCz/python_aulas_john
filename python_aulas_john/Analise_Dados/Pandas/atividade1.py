import pandas as pd
# Minha tentativa de resolução
# url_filmes = "netlix_titles.csv"
# df_filmes = pd.read_csv(url_filmes)
# print("Primeiras 7 linhas do DataFrame")
# print(df_filmes.head(7))
# print("\nInformações sobre o DataFrame")
# print(df_filmes.info())
# print(f"\nO dataFrame de filmes tem {df_filmes.shape[0]} e colunas {df_filmes.shape[1]}") 
# print("Rating do DataFrame:")
# print(df_filmes.describe('Rating'))


# Carrega o DataFrame a partir do arquivo CSV
url_filmes = "netflix_titles.csv"  # Certifique-se de que o nome do arquivo está correto (Netflix está escrito errado aqui)
df_filmes = pd.read_csv(url_filmes)

# 1 e 2. Exibe as primeiras 7 linhas
print("Primeiras 7 linhas do DataFrame")
print(df_filmes.head(7))

# 3. Exibe informações sobre o DataFrame, incluindo tipos de dados e valores nulos
print("\nInformações sobre o DataFrame")
df_filmes.info()

# Para contar quantas colunas têm valores ausentes:
colunas_com_nulos = df_filmes.isnull().any()
qtd_colunas_com_nulos = colunas_com_nulos.sum()
print(f"\nNúmero de colunas com valores ausentes: {qtd_colunas_com_nulos}")

# 4. Verifica número de linhas (filmes) e colunas (características)
print(f"\nO DataFrame tem {df_filmes.shape[0]} filmes e {df_filmes.shape[1]} colunas")

# 5. Estatísticas da coluna 'Rating'
print("\nEstatísticas da coluna 'Rating':")
print(df_filmes.describe())
