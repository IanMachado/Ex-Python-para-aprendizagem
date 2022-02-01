print('\033[1;35m{:*^40}'.format(' LOJAS MACHADO '))
val = float(input('\033[1;97mInforme o valor das compras: \033[m'))

print('\033[1;30mFORMAS DE PAGAMENTO\033[m\n'
      '\033[1;33m[ 1 ]\033[m à vista dinheiro/cheque\n'
      '\033[1;33m[ 2 ]\033[m à vista no cartão\n'
      '\033[1;33m[ 3 ]\033[m 2x no cartão\n'
      '\033[1;33m[ 4 ]\033[m 3x ou mais no cartão')

pag = int(input('\033[1;34mQual a opção?\033[m '))

if (pag != 1 and pag != 2) and (pag != 3 and pag != 4) :
    print('\033[1;31mForma de pagamento não identificada, tente novamente...\033[m')
    quit()
if pag == 1:
    print('\033[1;32mSua compra de R${} vai custar R${} à vista.'.format(val,val-(0.1*val)))
elif pag == 2:
    print('[1;32mSua compra de R${} vai custar R${} à vista no cartão.'.format(val,val-(0.05*val)))
elif pag == 3:
    print('[1;32mSua compra vai custar R${} parcelada 2x no cartão.\033[m'.format(val))
elif pag == 4:
    qts = int(input('\033[1;34mQuantas parcelas?\033[m '))
    print(f'\033[1;32mSua compra será parcelada com JUROS em {qts}x de R${(val+(val*0.2))/ qts}')
    print(f'Sua compra custará R${val+(val*0.2)} no total\033[m')
