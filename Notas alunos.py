notas = []

opcao = 0

while opcao != 3:
    print(' 1- Inserir nota  \n 2- Exibir notas   \n 3- Sair' )
    opcao = int(input('Digite sua opção: '))

    if opcao == 1:
        notas.append(float(input('Adicione uma nota: ')))

   
    elif opcao == 2:
        print('Notas:')
        for nota in notas:
         print(nota)
    elif opcao == 3:
        print('Programa finalizado!')

    elif opcao != 1 and opcao != 2 and opcao != 3:
        print('Comando inválido')

