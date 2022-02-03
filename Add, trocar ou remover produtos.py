# Adicionar: lista.append(item)

# Remover: lista.remove(item)
# Removendo pelo índice: item_removido = lista.pop(índice)


lista = ['iphone 11', 'apple watch', 'airpods', 'ipad', 'mac book', 'apple tv', 'iphone 12']

# item_removido = lista.pop(0)
# print(lista)
# print(f'Excluímos o item {item_removido} da lista')
print(lista)
opcao = input('Deseja Adicionar, Trocar ou Remover um item da lista? ')
opcao = opcao.lower()

if opcao == 'adicionar':
    produto = input('Nome do novo produto: ').lower()
    lista.append(produto)

elif opcao == 'trocar':
    produto_removido = input('Nome do produto que será trocado: ').lower()
    try:
        i = lista.index(produto_removido)
        produto_adicionado = input('Nome do produto que será adicionado no lugar: ').lower()
        lista[i] = produto_adicionado
    except:
        print('Produto não encontrado, tente novamente!')
        quit()

elif opcao == 'remover':
    try:
        produto_removido = input('Nome do produto que será removido: ').lower()
        lista.remove(produto_removido)
    except:
        print('Produto não encontrado, tente novamente')
        quit()

else:
    print('Comando inválido, tente novamente')
    quit()
print(lista)