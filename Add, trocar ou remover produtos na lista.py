# Adicionar: lista.append(item)

# Remover: lista.remove(item)
# Removendo pelo índice: item_removido = lista.pop(índice)


lista = ['iphone 11', 'apple watch', 'airpods', 'ipad', 'mac book', 'apple tv', 'iphone 12']

#item_removido = lista.pop(0)
#print(lista)
#print(f'Excluímos o item {item_removido} da lista')
print(lista)
opcao = input('Deseja Adicionar, Trocar ou Remover um item da lista? ')
opcao = opcao.lower()

if opcao == 'adicionar':
   produto = input('Nome do novo produto: ').lower()
   lista.append(produto)

elif opcao == 'trocar':
   produto_removido = input('Nome do produto que será trocado: ').lower()
   while produto_removido not in lista:
       print('Produto não encontrado, tente novamente!')
       produto_removido = input('Nome do produto que será trocado: ')
   i = lista.index(produto_removido)
   produto_adicionado = input('Nome do produto que será adicionado no lugar: ').lower()
   lista[i] = produto_adicionado

elif opcao == 'remover':
    produto_removido = input('Nome do produto que será removido: ')
    while produto_removido not in lista:
        print('Produto não encontrado, tente novamente')
        produto_removido = input('Nome do produto que será removido: ')
    lista.remove(produto_removido)

else:
    print('Comando inválido, tente novamente')
    quit()
print(lista)