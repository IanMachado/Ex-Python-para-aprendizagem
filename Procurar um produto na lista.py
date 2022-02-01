product = ['tv', 'geladeira', 'guarda roupa', 'fogão', 'sofá', 'celular', 'notebook']
stock = ['50', '20', '35', '60', '45', '150', '200']

# relacionando um estoque com seu índice

##print(estoque[2])
# tem 35 guarda roupa, mas e se eu não soubesse o índice do guarda roupa? em uma lista grande

i = product.index('guarda roupa')
qtd_stock = stock[i]
# index irá achar o índice do item na lista, que nesse caso é 2

#print(f'A quantidade em estoque de guarda-roupa é {qtd_estoque}')


name_of_product = input('name of product: ').lower()

if name_of_product not in product:
    print('Product not found!')

else:
    j = product.index(name_of_product)
    pct_stk = stock[j]
    print(f'The quantity in stock of {name_of_product} is {pct_stk} ')
