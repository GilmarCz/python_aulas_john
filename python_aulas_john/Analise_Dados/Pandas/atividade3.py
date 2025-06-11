import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")

#Converter 'Meta_score' para numerico se necessario
df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'],errors='coerce')

#1 Criar uma nova coluna
df_filmes['Rating_Metascore_Diff'] = (df_filmes['IMDB_Rating'] - df_filmes['Meta_score']/10)
print(f"\nO DataFrame agora tem uma nova coluna: ")
print(df_filmes.head())

#2 Mostras as colunas 'Title' 'Rating' 'Metascore' e a nova 'Rating_Metascore_Diff'
df_filmes_2 = df_filmes[['Series_Title', 'IMDB_Rating', 'Meta_score', 'Rating_Metascore_Diff']]
print(f"\nDataFrame com titulo, avaliação, meta, avaliação_meta: ")
print(df_filmes_2.head())

#3 Remova a coluna Overview, criar um novo dataframe para não alterar a original
new_df_filmes = df_filmes.copy()
print(new_df_filmes.columns.tolist())
new_df_filmes = new_df_filmes.drop('Overview', axis=1)
#new_df_filmes = new_df_filmes.drop(columns='Overview')
print(f"\n#3 Criação de um novo DataFrame e remoção da coluna 'Overview'")
print(new_df_filmes.columns.tolist())

#4 Renomear a coluna 'No_of_Votes' para 'Numero_Votos'
print(df_filmes.columns.tolist())
df_filmes.rename(columns={'No_of_Votes': 'Numero_Votos'}, inplace=True)
print(f"\n#4 Renomear a coluna 'No_of_Votes' para 'Numero_Votos'")
print(df_filmes.columns.tolist())