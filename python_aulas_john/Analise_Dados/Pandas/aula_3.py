import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")

# Selecionando a coluna 'Title'
titulos_filmes = df_filmes['Series_Title']
print("Primeiros cinco titulos")
print(titulos_filmes.head())

# Selecionando multiplas colunas
filmes_selecionados = df_filmes[['Series_Title','Genre','IMDB_Rating']]
print(f"\nDataFrame com titulo, genero e nota")
print(filmes_selecionados.head())

# Selecinando a primeira linha=(registro) [coluna = atributo]
# iloc é usado para selecionar linhas por indice numérico
Primeiro_filme = df_filmes.iloc[0]
print(f"\nPrimeiro filme (Linha completa)")
print(Primeiro_filme)

# Selecionar as 3 primeiras linhas
tres_primeiros_filme = df_filmes.iloc[0:3]
print(f"\nTres primeiro filme (DataFrame): ")
print(tres_primeiros_filme)

# Selecionando linhas e colunas especificas
selecao_especifica = df_filmes.iloc[[0,3],[1,4,5,6]]
print(f"\nPrintando uma seleção especifica, linha 0 e 3, e coluna 5 e 6")
print(selecao_especifica)

# Selecionando Dados com .loc
# Localiza os dados pelos rótulos 
df_filmes_idx = df_filmes.set_index('Series_Title')
print(f"\nDefinimos os indice agora como Series Titles")
print(df_filmes_idx.head())

Poderoso = df_filmes_idx.loc['The Godfather']
print(f"\nDados do filme: Godfather: ")
print(Poderoso)

# Filtrar os dados baseados em condições (Boolean indexing0)
df_filmes_bem_avaliados = df_filmes[df_filmes['IMDB_Rating'] >= 9]
print(f"\nFilmes com notas >= 9 (Primeiras Linhas)")
print(df_filmes_bem_avaliados['Series_Title'].head())
df_filmes_bem_avaliados1 = df_filmes[df_filmes['IMDB_Rating'] < 8.5]
print(f"\nFilmes com notas < 8.5 (Primeiras Linhas)")
print(df_filmes_bem_avaliados1[['Series_Title','Genre']].head())

# Filmes que tem gênero 'Action'
filmes_acao = df_filmes[df_filmes['Genre'].str.contains('Action', na=False)] # na=False limpa os dados que estão vazios
print(f"\nFilmes que contem o genero 'Action'")
print(filmes_acao[['Series_Title','Genre']].head())