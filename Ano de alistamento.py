from datetime import date
atual = date.today().year
ano = int(input('Ano de nascimento: '))
print(f'Quem nasceu em {ano} completará {atual-ano} anos em {atual}.')
if atual - ano > 18 :
    print(f'Deveria ter se alistado há {atual-ano-18} anos. \n'
          f'Seu alistamento foi em {ano + 18}.')
elif atual - ano < 18:
    print(f'Deverá se alistar em {(atual-ano-18) * -1} anos. \n'
          f'Seu alistamento será em {ano + 18}.')
elif atual - ano == 18:
    print(f'Deverá se alistar IMEDIATAMENTE!')
