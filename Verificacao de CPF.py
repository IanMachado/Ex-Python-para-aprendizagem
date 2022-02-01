cpf = input('Insira seu CPF(Digite apenas números): ')

cpf = cpf.replace('-','')
cpf = cpf.replace('.','')
cpf = cpf.split()
cpf = ''.join(cpf)

print(cpf)
if len(cpf) == 11 and cpf.isnumeric() :
    print('Continua')

else:
    print('Informe seu CPF corretamente e digite apenas números!')

print(type(cpf))

