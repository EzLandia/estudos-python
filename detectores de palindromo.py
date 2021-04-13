itens = str(input('Digite os itens, separando por espaço: ')).split()
quantidade = len(itens)
cont = 0
for c in range(0,quantidade):
    selecionar = itens[c]
    inverter = selecionar[::-1]
    if itens[c] == inverter:
        print(f'\33[1:32m{itens[c]} é um palíndromo!\33[m')
        cont = cont+1
    else:
        print(f'\33[1:31m{itens[c]} não é um palíndromo!')
print(' \n \33[1:30:42m Temos um total de {} palíndromos\33[m'.format(cont))
