itens = list()
finalizar = 0
while finalizar < 1:
    itens.append(str(input('Digite algo para verificar se é um palíndromo: ')))
    print('Quando desejar consultar o resultado, Digite F')
    if itens.count('F') == 1:
        finalizar = finalizar + 1
quantidade = len(itens)
cont = 0
for c in range(0,quantidade):
    minus = itens[c].lower()
    junto = minus.replace(' ', '')
    selecionar = junto
    inverter = selecionar[::-1]
    if minus.replace(' ', '') == inverter:
        print(f'\33[1:32m{itens[c]} é um palíndromo!\33[m')
        cont = cont+1
    else:
        print(f'\33[1:31m{itens[c]} não é um palíndromo!')
print(' \n \33[1:30:42m Temos um total de {} palíndromos\33[m'.format(cont))
