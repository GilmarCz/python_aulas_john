""" Crie um programa em Python que:
Possua uma senha pré-definida no código, como por exemplo: "python123".
Peça ao usuário que digite a senha.
O usuário terá no máximo 3 tentativas para acertar a senha.
Se acertar, o programa deve exibir a mensagem:
"Acesso concedido!"
Se errar todas as tentativas, o programa deve exibir:
"Acesso bloqueado! Tentativas esgotadas."
Use a estrutura de repetição while para controlar o número de tentativas.
🧪 Exemplo de saída esperada:
yamlCopiarEditarDigite a senha: admin Senha incorreta. Tentativas restantes: 2 Digite a senha: 1234 Senha incorreta. Tentativas restantes: 1 Digite a senha: python123 Acesso concedido! 
ou:
yamlCopiarEditarDigite a senha: admin Senha incorreta. Tentativas restantes: 2 Digite a senha: python1 Senha incorreta. Tentativas restantes: 1 Digite a senha: 0000 Acesso bloqueado! Tentativas esgotadas. """

senha_correta = "python123"
tentativas = 3

while tentativas > 0:
    senha_usuario = input("Digite a senha: ")
    if senha_usuario == senha_correta:
        print("Acesso concedido!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Senha incorreta. Tentativas restantes: {tentativas}")
        else:
            print("Acesso bloqueado! Tentativas esgotadas.")
            