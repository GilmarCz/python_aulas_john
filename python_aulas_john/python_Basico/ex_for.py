""" Crie um programa em Python que:
Peça ao usuário para digitar um número inteiro entre 1 e 10.
Verifique se o número está dentro do intervalo permitido:
Se estiver, imprima a tabuada completa desse número (de 1 a 10).
Se não estiver, exiba uma mensagem de erro informando que o número deve estar entre 1 e 10.
Use estrutura de repetição (for) para imprimir a tabuada.
Organize o layout da saída para ficar bem formatado.
🧪 Exemplo de saída esperada:
Suponha que o usuário digitou 3:
----- Tabuada do 3 -----
   3 x 1 = 3
   3 x 2 = 6
   3 x 3 = 9
   3 x 4 = 12
   3 x 5 = 15
   3 x 6 = 18
   3 x 7 = 21
   3 x 8 = 24
   3 x 9 = 27
   3 x 10 = 30
------------------------ """

tabuada = int(input("Digite um número inteiro entre 1 e 10: "))
if 1 <= tabuada <= 10:
    print(f"----- Tabuada do {tabuada} -----")
    for i in range(1, 11):
        print(f"   {tabuada} x {i} = {tabuada * i}")
    print("------------------------")
else:
    print("Erro: O número deve estar entre 1 e 10.")