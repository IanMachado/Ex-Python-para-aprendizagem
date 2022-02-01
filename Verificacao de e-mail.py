name = input('Your first name: ')
email = input('Your best e-mail: ')

if name and email :
   if '@' in email and '.' in email[email.find('@'):]:
       print('Cadastro concluído')
   else:
       print('Email inválido')

# os dois pontos depois no find irá mostrar o q vem depois do @
# se os dois pontos fosse email[:emial... iria mostrar o q vem antes do @
else:
    print('Por favor, digite o nome/email corretamente!')