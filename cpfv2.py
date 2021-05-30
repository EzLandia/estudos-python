def multiplicar(list, i, f, p):
    dg = 0
    s = 0
    for d in range(i, f, p):
        s += list[dg]*d
        dg += 1
    return s


while True:
    cpf = []
    num = list(input('Digite seu CPF: '))
    for d in num:
        if d.isnumeric() == True:
            cpf.append(int(d))
    print(f'\nCPF informado: {cpf[0:11]}',end='')
    if len(cpf) == 11:
        print('\nVerificando se esse CPF é válido...\n')
        break
    else:
        print('\nParece que você não digitou um CPF, tente novamente.\n')
v1 = 11-(multiplicar(cpf, 10, 1, -1)%11)
if v1 >= 10: v1 = 0
v2 = 11-((multiplicar(cpf, 11, 2, -1)+(v1*2))%11)
if v2 >= 10: v2 = 0
if v1 == cpf[9] and v2 == cpf[10]:
    print('CPF VÁLIDO!')
else:
    print('CPF INVALIDO!')
