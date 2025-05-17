# Atividade 19
nome = "Gilmar"
cidade = "Curitiba"
estado = "Paraná"
cep = "81000-000"
dig_nome = input("Digite um nome: ")

if nome == dig_nome:
    print(f"nome: {dig_nome}, \ncidade: {cidade}, \nestado: {estado}, \nCEP: {cep}.")
else:
    print("Esse usuário não existe no nosso BD")