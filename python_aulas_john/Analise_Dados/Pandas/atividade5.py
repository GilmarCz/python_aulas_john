import pandas as pd
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")
print("\n" + "="*60 + "\n")

#1 Conte quantos filmes cada diretor dirigiu usando a coluna 'Director'
# Mostre os 5 diretores mais frequentes no DF
contagem_diretores = df_filmes['Director'].value_counts()
print(f"\nOs 5 diretores mais frequentes: ")
print(contagem_diretores.head())
print("\n" + "="*60 + "\n")

#2 Ordene os filmes pelo tempo de duração 'Runtime' em ordem decrescente e mostre os 10 filmes mais longos
df_filmes['Runtime'] = df_filmes['Runtime'].str.replace(' min','')
df_filmes['Runtime'] = pd.to_numeric(df_filmes['Runtime'],errors='coerce')
df_ordenado_por_duracao = df_filmes.sort_values(by='Runtime', ascending=False).head(10)
print(f"\nTop 10 filmes por duração 'Runtime': ")
print(df_ordenado_por_duracao[['Series_Title','Runtime']])
print("\n" + "="*60 + "\n")

#3 Ordene os filmes por 'Certificate'(ordem alfabetica) e em seguida, por 'Meta_score' em ordem decrescente. mostre os 5 primeiros resultados
df_ordenado_por_duas_colunas = df_filmes.sort_values(by=['Certificate','Meta_score'], ascending=[True,False]).head()
print(f"\nTop 5 filmes por ordem alfabetica e meta: ")
print(df_ordenado_por_duas_colunas[['Series_Title','Certificate']])
print("\n" + "="*60 + "\n")

#4 converter as colunas 'Meta_score' e 'Runtime' para tipo numerico, tratando valores invalidos com errors='coerce'
# Agrupe os dados por 'Certificate', calcule
# a média de 'Runtime'
# a média de 'Meta_score'
# o total de filmes por certificado
# df_filmes['Runtime'] = df_filmes['Runtime'].str.replace(' min','')
df_filmes['Meta_score'] = pd.to_numeric(df_filmes['Meta_score'],errors='coerce')
# df_filmes['Runtime'] = pd.to_numeric(df_filmes['Runtime'],errors='coerce')

metricas = df_filmes.groupby('Certificate').agg(
    Media_Duracao=('Runtime','mean'),
    Media_Meta=('Meta_score','mean'),
    Total_filmes=('Certificate','count')
    )
print(metricas)
print("\n" + "="*60 + "\n")