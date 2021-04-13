#PALINCHECK V1.0
#TIVE QUE REVER A AULA DE MANIPULAÇÃO DE STRINGS 3 VEZES PRA CONCLUIR ISSO AQUI
import time
print('Verificador de palíndromo')
#RECEBE A FRASE, TIRA OS ESPAÇOS DAS EXTREMIDADES, DEIXA MINUSCULO E SEPARA NUMA LISTA.
frase = str(input('Digite uma frase: ')).strip().lower().split()
#UNE OS ITENS DA LISTA NUMA UNICA CADEIA DE CARACTERES
juntosemespaco = ''.join(frase)
#INVERTE O TEXTO
inverter = juntosemespaco[::-1]
#INFORMA AO USUARIO A FRASE DIGITADA
print(f'Você digitou \33[1:30:43m{juntosemespaco}\33[m, estamos verificando se isso é um palíndromo :D')
time.sleep(1)
print('-=' *30)
time.sleep(1)
print('//' *30)
time.sleep(1)
print('\33[1:30:43m{}\33[m de trás para frente fica \33[1:30:43m{}\33[m \n'.format(juntosemespaco,inverter))
#VERIFICA A IGUALDADE DA FRASE DIGITADA COM A FRASE INVERTIDA E INFORMA O RESULTADO AO USUARIO.
if juntosemespaco == inverter:
    print('\33[1:30:42mTemos um palíndromo :DDDD\33[m')
    time.sleep(30)
else:
    print('\33[1:30:41mIsso não é um palíndromo!\33[m')
    time.sleep(30)
