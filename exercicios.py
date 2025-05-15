
#1. Olá, mundo!
""" Exercício 1.1
Crie um programa que exiba a seguinte mensagem na tela:
Bem-vindo ao mundo da programação! """

print("Bem-vindo ao mundo da programação!") 

#2. Variáveis e Tipos de Dados
""" Exercício 2.1
Declare variáveis para armazenar:
Seu nome
Sua idade
Sua altura
Se você está estudando Python (valor booleano)
Depois, exiba essas informações usando o comando print().
Exercício 2.2
Crie duas variáveis com números inteiros, some-as e mostre o resultado. """

#Exercício 2.1
nome = "Gilmar"
idade = 46  
altura = 1.61
estudando_python = True
print("Nome:", nome , 
      "\nIdade:", idade, 
      "\nAltura:", altura, 
      "\nEstudando Python:", estudando_python)

#Exercício 2.2
inteiro = 10
decimal = 5.5
soma = inteiro + decimal
print("Soma:", soma)

""" 3. Entrada de Dados
Exercício 3.1
Solicite ao usuário que informe seu nome e idade. Em seguida, mostre a mensagem:
Olá, [nome]! Você tem [idade] anos.
Exercício 3.2
Peça dois números ao usuário, some-os e exiba o resultado na tela. """

#Exercício 3.1
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))   
print("Olá,", nome, "! Você tem", idade, "anos.")   

#Exercício 3.2
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))  
soma = num1 + num2
print("A soma é:", soma)

""" 4. Operadores Matemáticos
Exercício 4.1
Peça um número ao usuário e exiba:
O dobro
O triplo
A raiz quadrada
Exercício 4.2
Crie um programa que calcule o IMC (Índice de Massa Corporal).
Fórmula: IMC = peso / altura ** 2 """

#Exercício 4.1
num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raiz_quadrada = num ** 0.5
print("Dobro:", dobro, 
      "\nTriplo:", triplo, 
      "\nRaiz quadrada:", raiz_quadrada)

#Exercício 4.2
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
print("Seu IMC é:", imc)

""" 5. Condicionais
Exercício 5.1
Peça a idade do usuário e classifique conforme a faixa etária:
Criança (até 12 anos)
Adolescente (13 a 17 anos)
Adulto (18 a 59 anos)
Idoso (60 anos ou mais)
Exercício 5.2
Peça uma nota entre 0 e 10 e informe:
Aprovado (nota maior ou igual a 7)
Recuperação (nota entre 5 e 6.9)
Reprovado (nota menor que 5) """

#Exercício 5.1
idade = int(input("Digite sua idade: "))
if idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida")

        
#Exercício 5.2
nota = float(input("Digite sua nota (0 a 10): "))
if 0 <= nota < 5:
    print("Reprovado")
elif 5 <= nota < 7:
    print("Recuperação")
elif 7 <= nota <= 10:
    print("Aprovado")
else:
    print("Nota inválida")
    
    
""" 6. Laços de Repetição
Exercício 6.1 – While
Faça um programa que conte de 1 a 10 utilizando o laço while.
Exercício 6.2 – For
Solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando o laço for. """

#Exercício 6.1
contador = 1
while contador <= 10:
    print(contador)
    contador += 1
    
    
#Exercício 6.2
num = int(input("Digite um número: "))  
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")  
