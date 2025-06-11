import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")
print("\n" + "="*60 + "\n")

#1 verifique quantos valores ausentes existem nas colunas 'Gross' e 'Meta_score'
df_filmes1 = df_filmes[['Meta_score','Gross']]
print(f"Contagem de valores ausentes por colunas: ")
print(df_filmes1.isna().sum())
print("\n" + "="*60 + "\n")

#2 cria um novo DF chamado df_filmes_completo removendo todas as linhas que tenham NAN. Quantas linhas restam?
df_filmes_completo = df_filmes.copy()
print(f"\nNúmeros de linhas originais: {len(df_filmes_completo)}")
print("\n" + "="*60 + "\n")
df_filmes_completo.dropna(inplace=True) # "dropa" linhas que tem dados ausentes|invalidas
print(f"\nNúmeros de linhas depois do drop: {len(df_filmes_completo)}")
print("\n" + "="*60 + "\n")

#3 crie DF chamado df_filmes_preenchido_media . Nele preencha os valores ausentes de 'Gross' com a média 
#dessa coluna e os valores ausentes de 'Meta_score' com a mediana dessa coluna. verifique se ainda há Nan nessas colunas