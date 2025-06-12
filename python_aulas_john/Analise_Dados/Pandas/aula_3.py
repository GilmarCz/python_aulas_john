import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")
print("\n" + "="*60 + "\n")

# Selecionando a coluna 'Title'
titulos_filmes = df_filmes['Series_Title']
print("Primeiros cinco titulos")
print(titulos_filmes.head())
print("\n" + "="*60 + "\n")

# Selecionando multiplas colunas
filmes_selecionados = df_filmes[['Series_Title','Genre','IMDB_Rating']]
print(f"\nDataFrame com titulo, genero e nota")
print(filmes_selecionados.head())
print("\n" + "="*60 + "\n")

# Selecinando a primeira linha=(registro) [coluna = atributo]
# iloc é usado para selecionar linhas por indice numérico
Primeiro_filme = df_filmes.iloc[0]
print(f"\nPrimeiro filme (Linha completa)")
print(Primeiro_filme)
print("\n" + "="*60 + "\n")

# Selecionar as 3 primeiras linhas
tres_primeiros_filme = df_filmes.iloc[0:3]
print(f"\nTres primeiro filme (DataFrame): ")
print(tres_primeiros_filme)
print("\n" + "="*60 + "\n")

# Selecionando linhas e colunas especificas
selecao_especifica = df_filmes.iloc[[0,3],[1,4,5,6]]
print(f"\nPrintando uma seleção especifica, linha 0 e 3, e coluna 5 e 6")
print(selecao_especifica)
print("\n" + "="*60 + "\n")

# Selecionando Dados com .loc
# Localiza os dados pelos rótulos 
df_filmes_idx = df_filmes.set_index('Series_Title')
print(f"\nDefinimos os indice agora como Series Titles")
print(df_filmes_idx.head())
print("\n" + "="*60 + "\n")

Poderoso = df_filmes_idx.loc['The Godfather']
print(f"\nDados do filme: Godfather: ")
print(Poderoso)
print("\n" + "="*60 + "\n")

# Filtrar os dados baseados em condições (Boolean indexing0)
df_filmes_bem_avaliados = df_filmes[df_filmes['IMDB_Rating'] >= 9]
print(f"\nFilmes com notas >= 9 (Primeiras Linhas)")
print(df_filmes_bem_avaliados['Series_Title'].head())
df_filmes_bem_avaliados1 = df_filmes[df_filmes['IMDB_Rating'] < 8.5]
print(f"\nFilmes com notas < 8.5 (Primeiras Linhas)")
print(df_filmes_bem_avaliados1[['Series_Title','Genre']].head())
print("\n" + "="*60 + "\n")

# Filmes que tem gênero 'Action'
filmes_acao = df_filmes[df_filmes['Genre'].str.contains('Action', na=False)] # na=False limpa os dados que estão vazios
print(f"\nFilmes que contem o genero 'Action'")
print(filmes_acao[['Series_Title','Genre']].head())
print("\n" + "="*60 + "\n")

ano_filme = df_filmes.iloc[9]
print(type(ano_filme['Released_Year']))
print("\n" + "="*60 + "\n")

#Criar nova coluna
df_filmes['Rating_x_10'] = df_filmes['IMDB_Rating'] * 10
print(f"\nO DataFrame agora tem uma nova coluna: ")
print(df_filmes.head())
print("\n" + "="*60 + "\n")

# #Conversão da coluna Gross para float e ignorando erros caso falhar
# df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'],errors='coerce')

# #Agora convertido o numero Gross em numero, é mais seguro fazer a comparação
# df_filmes['Alta_Receita'] = df_filmes['Gross'] > 1000
# print(f"\nDataFrame com uma nova coluna 'Alta Receita' (primeiras linhas)")
# print(df_filmes.head())
print("\n" + "="*60 + "\n")

# Drop
# Método drop remove uma linha (registro) ou coluna
# axis=1 exclui a coluna
df_filmes = df_filmes.drop('Poster_Link', axis=1)
print(df_filmes.head())
print("\n" + "="*60 + "\n")

# axis=0 exclui o registro
df_filmes = df_filmes.drop(4, axis=0)
print(df_filmes.head())
print("\n" + "="*60 + "\n")

# Lidando com dados Ausentes
# Verifica dados ausentes com .isna() .sum()
print(f"Contagem de valores ausentes por colunas: ")
print(df_filmes.isna().sum())
print("\n" + "="*60 + "\n")

# Removendo linhas/colunas
# criando uma cópia para não alterar a original
df_sem_nan_linhas = df_filmes.copy()
print("\n" + "="*60 + "\n")

# removendo todas as linhas que contenham qualquer valor NAN
df_sem_nan_linhas.dropna(inplace=True) # "dropa" linhas que tem dados ausentes|invalidas
print(f"\nNúmeros de linhas originais: {len(df_filmes)}")
print(f"\nNúmeros de linhas depois do drop: {len(df_sem_nan_linhas)}")
print("\n" + "="*60 + "\n")

# removendo colunas que tenham qualquer valor Nan
df_sem_nan_colunas = df_filmes.dropna(axis=1) # axis=1 colunas | axis=0 linhas
print(f"Colunas originais: {df_filmes.columns.tolist()}")
print(f"Colunas depois do drop: {df_sem_nan_colunas.columns.tolist()}")
print("\n" + "="*60 + "\n")

# Contando frequências de coluna
contagem_diretores = df_filmes['Director'].value_counts()
print(f"\nOs 10 diretores mais frequentes: ")
print(contagem_diretores.head(10))
print("\n" + "="*60 + "\n")

# Ordenando os filmes pela nota IMDB_Rating
df_ordenado_por_nota = df_filmes.sort_values(by='IMDB_Rating', ascending=False)
print(f"\nTop 5 filmes por nota 'IMBD_Rating': ")
print(df_ordenado_por_nota.head())
print("\n" + "="*60 + "\n")

# Ordenando os filmes por mais de uma coluna
df_ordenado_por_duas_colunas = df_filmes.sort_values(by=['Released_Year','Gross'], ascending=[False,True])
print(f"\nTop 5 filmes por ano e gross: ")
print(df_ordenado_por_duas_colunas.head())
print("\n" + "="*60 + "\n")

# Converter caso necessáro
df_filmes['Gross'] = df_filmes['Gross'].str.replace(',','')
df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'],errors='coerce')
df_filmes['IMDB_Rating'] = pd.to_numeric(df_filmes['IMDB_Rating'],errors='coerce')

# Calculando a média de IMDB e Gross para cada Released_Year
metricas_por_ano = df_filmes.groupby('Released_Year').agg(
    Media_Rating=('IMDB_Rating','mean'),
    Media_Receita=('Gross','mean'),
    Total_filmes=('Series_Title','count')
    )
print(metricas_por_ano)
print("\n" + "="*60 + "\n")

# Salvando em um arquivo CSV sem o indice
df_filmes.to_csv('meus_filmes_bem_avaliados.csv',index=False)
print(f"\nDataFrame salvo em 'meus_filmes_bem_avaliados.csv'")
print("\n" + "="*60 + "\n")