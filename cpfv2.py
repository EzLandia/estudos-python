def multiplicar(list, i, f, p):
    inicio = 0
    soma = 0
    for digito in range(i, f, p):
        soma += list[inicio]*digito # Multiplica e adiciona a soma a váriavel para verificação dos digitos.
        inicio += 1
    return soma


while True:
    cpf = []
    numero = list(input('Digite seu CPF: ')) # Pede ao usuario para informar o CPF a ser verificado.
    for digito in numero:
        if digito.isnumeric() == True: # Verifica na váriavel numero se os elementos são númericos.
            cpf.append(int(digito)) # Caso sejam númericos, são adicionados a lista cpf.
    print(f'\nCPF informado: {cpf[0:11]}',end='')
    if len(cpf) == 11: # Verifica se o tamanho da lista CPF contem 11 digitos, se sim, segue para verificação.
        print('\nVerificando se esse CPF é válido...\n')
        break
    else: # Caso o tamanho da lista tenha mais ou menos números, repete o loop e pede para inserir novamente.
        print('\nParece que você não digitou um CPF, tente novamente.\n')
verificador1 = 11-(multiplicar(cpf, 10, 1, -1)%11) # Envia os dados para a função multiplicar para obter o 1º digito verificador.
if verificador1 >= 10: verificador1 = 0 # Caso o primeiro digito seja igual ou maior que 10, ele é considerado zero.
verificador2 = 11-((multiplicar(cpf, 11, 2, -1)+(verificador1*2))%11) # Envia os dados para a função multiplicar e verifica o 2º digito.
if verificador2 >= 10: verificador2 = 0 # Caso o segundo digito seja igual ou maior a 10, tbm será considerado zero.
print('CPF VÁLIDO' if verificador1 == cpf[9] and verificador2 == cpf[10] else 'CPF INVALIDO') #Compara os digitos e mostra o resultado.
