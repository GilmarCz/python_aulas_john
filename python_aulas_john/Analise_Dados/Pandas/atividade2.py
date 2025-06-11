# minha tentativa de resolução
# import pandas as pd
# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)
# print("Dados carregados com sucesso!!!")

# #1
# titulos_filmes = df_filmes['Series_Title','Director','Year']
# print("Primeiros cinco titulos, diretores e ano")
# print(titulos_filmes.head())

# #2
# selecao_especifica = df_filmes.iloc[[10,11,12,13,14,15],[0,3]]
# print(f"\nPrintando uma seleção especifica, linhas 10,11,12,13,14 e 15 e colunas 0 e 3")
# print(selecao_especifica)

# #3
# df_filmes_idx = df_filmes.set_index('Rank')
# print(f"\nDefinimos os indice agora como Rank")
# print(df_filmes_idx.head())
# Rank = df_filmes_idx.loc['The Godfather']
# print(f"\nDados do filme: Godfather: ")
# print(Rank) 


# import pandas as pd
# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)
# print("Dados carregados com sucesso!!!")

# # --- Correção para o TypeError: Converter 'Released_Year' para numérico ---
# # É uma boa prática fazer isso após o carregamento, se você antecipa operações numéricas.
# df_filmes['Released_Year'] = pd.to_numeric(df_filmes['Released_Year'], errors='coerce')

# # Você também pode querer remover as linhas onde 'Released_Year' se tornou NaN,
# # se elas não forem relevantes para sua análise, ou tratá-las de forma específica.
# # Para este filtro, NaNs não satisfarão a condição.
# # df_filmes.dropna(subset=['Released_Year'], inplace=True) # Descomente se quiser remover linhas com anos NaN

# #1
# # Nomes de coluna corrigidos conforme a estrutura do CSV ('Series_Title', 'Released_Year')
# titulos_filmes = df_filmes[['Series_Title', 'Director', 'Released_Year']]
# print("\n#1 Primeiros cinco títulos, diretores e ano:")
# print(titulos_filmes.head())

# #2
# # Fatiamento corrigido para linhas (10 a 15 é 10:16) e colunas (0 a 3 é 0:4)
# selecao_especifica = df_filmes.iloc[10:16, 0:4]
# print(f"\n#2 Printando uma seleção específica, linhas 10 a 15 e colunas 0 a 3:")
# print(selecao_especifica)

# #3
# # Definir a coluna 'Rank' como o índice do df_filmes.
# # Lembre-se que o CSV que você forneceu não tem uma coluna 'Rank'.
# # Se 'Rank' for o índice padrão do DataFrame, você pode usá-lo diretamente ou
# # criar uma coluna 'Rank' a partir do índice se quiser que ela seja uma coluna nomeada.
# # Para esta atividade, vamos assumir que queremos usar o índice numérico padrão do pandas
# # como se fosse um "Rank" começando de 1.
# df_filmes_copy = df_filmes.copy() # Criar uma cópia para não alterar o original

# # Se 'Rank' não é uma coluna no seu CSV, vamos criar uma baseada no índice atual + 1
# # para simular o "Rank".
# df_filmes_copy['Rank'] = df_filmes_copy.index + 1
# df_filmes_idx = df_filmes_copy.set_index('Rank')

# print(f"\n#3 Definimos o índice agora como 'Rank' (primeiras linhas):")
# print(df_filmes_idx.head())

# # Usar .loc para selecionar filmes com Rank de 1 a 5 e mostrar 'Series_Title' e 'Gross'
# # Nota: 'Revenue(Millions)' na sua descrição provavelmente corresponde a 'Gross' no CSV.
# Rank_selection = df_filmes_idx.loc[1:5, ['Series_Title', 'Gross']]
# print(f"\nDados dos filmes com Rank de 1 a 5 (Title e Revenue):")
# print(Rank_selection)

# # Resetar o índice da cópia se necessário para operações futuras
# # df_filmes_idx_reset = df_filmes_idx.reset_index()


# #4
# # Filtrar o df_filmes para mostrar apenas filmes lançados ('Released_Year') a partir de 2016.
# # Como já convertemos 'Released_Year' para numérico, esta parte agora funcionará.
# filmes_2016 = df_filmes[df_filmes['Released_Year'] >= 2016]
# print(f"\n#4 Filmes lançados a partir de 2016 (Primeiras Linhas - Título e Ano):")
# print(filmes_2016[['Series_Title', 'Released_Year']].head())

# import pandas as pd
# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)
# print("Dados carregados com sucesso!!!")

# #1
# titulos_filmes = df_filmes[["Series_Title","Director","Released_Year"]]
# print("#1 Primeiros cinco titulos, diretores e ano")
# print(titulos_filmes.head())

# #2
# selecao_especifica = df_filmes.iloc[[10,11,12,13,14,15],[0,1,2,3]]
# print(f"\n#2 Printando uma seleção especifica, linhas 10,11,12,13,14 e 15 e colunas 0,1,2 e 3")
# print(selecao_especifica)

# #3
# # Não há coluna \'Rank\'. Acessando o filme no índice 5 (equivalente ao Rank 6).
# print(f"\n#3 Não há coluna \'Rank\'. Acessando o filme no índice 5 (equivalente ao Rank 6).")
# filme_rank_6 = df_filmes.loc[5, ["Series_Title", "Gross"]]
# print(f"\nDados do filme: ")
# print(filme_rank_6)

# #4
# df_filmes["Released_Year"] = pd.to_numeric(df_filmes["Released_Year"], errors="coerce")
# filmes_2016 = df_filmes[df_filmes["Released_Year"] >= 2016]
# print(f"\n#4 Filmes a partir de 2016 ")
# print(filmes_2016[['Series_Title', 'Released_Year']].head())

# resolução John
# import pandas as pd
# url_filmes = "IMDB-Movie-Data.csv"
# df_filmes = pd.read_csv(url_filmes)

# # 1 - Selecionar apenas as colunas desejadas e mostrar as 5 primeiras linhas
# colunas_selecionadas = df_filmes[['Series_Title', 'Director', 'Released_Year']]
# print("1 - Título, Diretor e Ano:")
# print(colunas_selecionadas.head())

# # 2 - Subconjunto específico usando iloc
# sub_conjunto_iloc = df_filmes.iloc[10:16, 0:4]
# print("\n2 - Subconjunto (linhas 10 a 15, colunas 0 a 3):")
# print(sub_conjunto_iloc)

# # 3 - Definir 'IMDB_Rating' como índice e mostrar 'Series_Title' e 'Gross'
# df_temp = df_filmes.set_index('IMDB_Rating')
# print("\n3 - Usando 'IMDB_Rating' como índice:")
# print(df_temp[['Series_Title', 'Gross']].head())

# # 4 - Filtrar filmes lançados a partir de 2016
# df_filmes['Released_Year'] = pd.to_numeric(df_filmes['Released_Year'], errors='coerce')
# filmes2016 = df_filmes[df_filmes['Released_Year'] >= 2016][['Series_Title', 'Released_Year']]
# print("\n4 - Filmes lançados em 2016 ou depois:")
# print(filmes2016)

import pandas as pd

# Carregando os dados
url_filmes = "IMDB-Movie-Data.csv"
df_filmes = pd.read_csv(url_filmes)
print("Dados carregados com sucesso!!!")
print(f"Shape do DataFrame: {df_filmes.shape}")
print(f"Colunas disponíveis: {list(df_filmes.columns)}")
print("\n" + "="*60 + "\n")

# 1. Selecionar apenas as colunas 'Series_Title', 'Director' e 'Released_Year'
print("1. PRIMEIRAS 5 LINHAS COM TÍTULO, DIRETOR E ANO:")
titulos_filmes = df_filmes[['Series_Title', 'Director', 'Released_Year']]
print(titulos_filmes.head())
print("\n" + "="*60 + "\n")

# 2. Usando .iloc selecionar filmes nas posições 10 a 15 e colunas 0 a 3
print("2. FILMES NAS POSIÇÕES 10-15 E COLUNAS 0-3:")
selecao_especifica = df_filmes.iloc[10:16, 0:4]  # 10:16 para incluir linha 15, 0:4 para incluir coluna 3
print(selecao_especifica)
print("\n" + "="*60 + "\n")

# 3. Definir coluna 'Rank' como índice e selecionar filmes com Rank 1 a 5
print("3. FILMES COM RANK 1-5 (TÍTULO E RECEITA):")
# Primeiro, vamos criar uma coluna Rank (já que não existe no CSV)
df_filmes_copy = df_filmes.copy()
df_filmes_copy['Rank'] = range(1, len(df_filmes_copy) + 1)

# Definir Rank como índice
df_filmes_idx = df_filmes_copy.set_index('Rank')

# Selecionar filmes com Rank 1 a 5 e mostrar Title e Gross (receita)
filmes_top5 = df_filmes_idx.loc[1:5, ['Series_Title', 'Gross']]
print(filmes_top5)

# Resetar o índice para não alterar o DataFrame original
df_filmes_idx.reset_index(inplace=True)
print("\n" + "="*60 + "\n")

# 4. Filtrar filmes lançados a partir de 2016
print("4. FILMES LANÇADOS A PARTIR DE 2016:")

# Primeiro, vamos verificar o tipo de dados da coluna Released_Year
print(f"Tipo de dados da coluna Released_Year: {df_filmes['Released_Year'].dtype}")
print(f"Exemplo de valores: {df_filmes['Released_Year'].head().tolist()}")

# Converter a coluna Released_Year para numérico
df_filmes['Released_Year'] = pd.to_numeric(df_filmes['Released_Year'], errors='coerce')

# Agora filtrar filmes lançados a partir de 2016
filmes_2016 = df_filmes[df_filmes['Released_Year'] >= 2016]
filmes_2016_titulo_ano = filmes_2016[['Series_Title', 'Released_Year']]
print(f"Total de filmes a partir de 2016: {len(filmes_2016_titulo_ano)}")
print(filmes_2016_titulo_ano)

# Informações adicionais sobre os dados
print("\n" + "="*60 + "\n")
print("INFORMAÇÕES ADICIONAIS:")
print(f"Período dos filmes: {df_filmes['Released_Year'].min()} - {df_filmes['Released_Year'].max()}")
print(f"Total de filmes no dataset: {len(df_filmes)}")
print(f"Filmes a partir de 2016: {len(filmes_2016)}")