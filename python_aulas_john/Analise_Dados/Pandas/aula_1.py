import pandas as pd

# Criando uma série
# idade = pd.Series([1,2,3,4,5,6])
# print(idade)

# idades_nome = pd.Series([1,2,3,4], index=['Ana','João','Maria','Carlos'])
# print(idades_nome)

# Data Frames
dados_alunos = {
    'Nome':['Ana','João','Maria','Carlos'],
    'Idade':[1,2,3,4],
    'Curso':['Engenharia','Medicina','Direito','Engenharia']
}
df_alunos = pd.DataFrame(dados_alunos)
print(df_alunos)