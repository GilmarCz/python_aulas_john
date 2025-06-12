# import pandas as pd
# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)
# print("Dados carregados com sucesso!!!")
# print("\n" + "="*60 + "\n")

# #1 verifique quantos valores ausentes existem nas colunas 'Gross' e 'Meta_score'
# df_filmes1 = df_filmes[['Meta_score','Gross']]
# print(f"Contagem de valores ausentes por colunas: ")
# print(df_filmes1.isna().sum())
# print("\n" + "="*60 + "\n")

# #2 cria um novo DF chamado df_filmes_completo removendo todas as linhas que tenham NAN. Quantas linhas restam?
# df_filmes_completo = df_filmes.copy()
# print(f"\nNúmeros de linhas originais: {len(df_filmes_completo)}")
# print("\n" + "="*60 + "\n")
# df_filmes_completo.dropna(inplace=True) # "dropa" linhas que tem dados ausentes|invalidas
# print(f"\nNúmeros de linhas depois do drop: {len(df_filmes_completo)}")
# print("\n" + "="*60 + "\n")

# #3 crie DF chamado df_filmes_preenchido_media . Nele preencha os valores ausentes de 'Gross' com a média 
# #dessa coluna e os valores ausentes de 'Meta_score' com a mediana dessa coluna. verifique se ainda há Nan nessas colunas
# df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')
# df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')

# # 3 - Preencher valores ausentes
# df_filmes_preenchido_media = df_filmes.copy()

# df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media["Gross"].fillna(df_filmes_preenchido_media["Gross"].mean())
# df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media["Meta_score"].fillna(df_filmes_preenchido_media["Meta_score"].median())
# print("3 - Verificando se ainda há valores ausentes em 'Gross' e 'Meta_score':")
# print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())




# # # Preenche os valores ausentes em 'Gross' com a média da coluna
# # media_gross = df_filmes_preenchido_media['Gross'].mean()
# # df_filmes_preenchido_media['Gross'].fillna(media_gross, inplace=True)

# # # Preenche os valores ausentes em 'Meta_score' com a mediana da coluna
# # mediana_meta = df_filmes_preenchido_media['Meta_score'].median()
# # df_filmes_preenchido_media['Meta_score'].fillna(mediana_meta, inplace=True)

# # # Verificar se ainda há valores ausentes
# # print("3 - Verificando se ainda há valores ausentes em 'Gross' e 'Meta_score':")
# # print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())

import pandas as pd

url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")
print("\n" + "="*60 + "\n")

# Verificar valores ausentes
df_filmes1 = df_filmes[['Meta_score','Gross']]
print(f"Contagem de valores ausentes por colunas: ")
print(df_filmes1.isna().sum())
print("\n" + "="*60 + "\n")

# Remover linhas com NaN
df_filmes_completo = df_filmes.copy()
print(f"\nNúmeros de linhas originais: {len(df_filmes_completo)}")
df_filmes_completo.dropna(inplace=True)
print(f"\nNúmeros de linhas depois do drop: {len(df_filmes_completo)}")
print("\n" + "="*60 + "\n")

# Limpar valores da coluna 'Gross'
#df_filmes['Gross'] = df_filmes['Gross'].replace('[\$,]', '', regex=True)
df_filmes['Gross'] = df_filmes['Gross'].str.replace(',','')
df_filmes['Gross'] = pd.to_numeric(df_filmes['Gross'], errors='coerce')
df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'], errors='coerce')

# Preencher valores ausentes
df_filmes_preenchido_media = df_filmes.copy()
df_filmes_preenchido_media['Gross'] = df_filmes_preenchido_media['Gross'].fillna(df_filmes_preenchido_media['Gross'].mean())
df_filmes_preenchido_media['Meta_score'] = df_filmes_preenchido_media['Meta_score'].fillna(df_filmes_preenchido_media['Meta_score'].median())

# Verificar novamente
print("3 - Verificando se ainda há valores ausentes em 'Gross' e 'Meta_score':")
print(df_filmes_preenchido_media[['Gross', 'Meta_score']].isna().sum())
