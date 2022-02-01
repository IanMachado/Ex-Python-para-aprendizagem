product = ['tv', 'geladeira', 'guarda roupa', 'fogão', 'sofá', 'celular', 'notebook']
stock = ['50', '20', '35', '60', '45', '150', '200']

name_of_product = input('name of product: ').lower()

if name_of_product not in product:
    print('Product not found!')

    
else:
    j = product.index(name_of_product)
    pct_stk = stock[j]
    print(f'The quantity in stock of {name_of_product} is {pct_stk} ')
