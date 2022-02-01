senha = str(input('Crie uma senha: '))
senha1 = str(input('Confirme sua senha: '))

while senha1 != senha:
    print('Senhas não compatíveis, tente novamente')
    senha = str(input('Crie uma senha: '))
    senha1 = str(input('Confirme sua senha: '))

else:
    print('Senha criada com sucesso!')

    print()

    senha2 = str(input('Digite sua senha: '))

    while senha2 != senha :
        senha2 = str(input('Senha incorrta, digite novamente: '))

    if senha2 == senha :
        print('Senha correta, seja bem vindo!')





























