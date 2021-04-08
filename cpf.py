#Apresentação :D
print("""
   _____  .__  .__                   ____  __.                .___            
  /  _  \ |  | |  | _____    ____   |    |/ _|____ _______  __| _/____  ____  
 /  /_\  \|  | |  | \__  \  /    \  |      < \__  \\_  __ \/ __ |/ __ \/ ___\ 
/    |    \  |_|  |__/ __ \|   |  \ |    |  \ / __ \|  | \/ /_/ \  ___|  \___ 
\____|__  /____/____(____  /___|  / |____|__ (____  /__|  \____ |\___  >___  >
        \/               \/     \/          \/    \/           \/    \/    \/ 
        \n Obrigado pelo desafio :D \n \n""")
#Recebe o CPF e separa e classifica como INT
numero = str(input('Insira seu CPF'))
cpf = str()
#Verifica se o CPF foi digitado com pontuação ou sem, e converte, se for o caso.
if (len(numero)) == 14:
    cpf = '{}{}{}{}'.format(numero[0:3],numero[4:7],numero[8:11],numero[12:14])
if (len(numero)) == 11:
    cpf = numero
#Confere se o CPF informado possui a quantidade certa de digitos.
if (len(cpf)) > 11:
    print('Ops, o CPF informado possui mais de 11 digitos! :S')
    exit(0)
elif (len(cpf)) < 11:
    print('Ops, o CPF informado possui menos de 11 digitos! :S')
    exit(0)
else:
    print('Verificando CPF...')
#Transforma os dados em INT
d1 = int(cpf[0])
d2 = int(cpf[1])
d3 = int(cpf[2])
d4 = int(cpf[3])
d5 = int(cpf[4])
d6 = int(cpf[5])
d7 = int(cpf[6])
d8 = int(cpf[7])
d9 = int(cpf[8])
d10 = int(cpf[9])
d11 = int(cpf[10])
#Multiplicação dos resultados (1 a 9)
n1 = d1*10
n2 = d2*9
n3 = d3*8
n4 = d4*7
n5 = d5*6
n6 = d6*5
n7 = d7*4
n8 = d8*3
n9 = d9*2
#Parte 2 da multiplicação
nd1 = d1*11
nd2 = d2*10
nd3 = d3*9
nd4 = d4*8
nd5 = d5*7
nd6 = d6*6
nd7 = d7*5
nd8 = d8*4
nd9 = d9*3
#Calculo dos digitos
dv1 = n1+n2+n3+n4+n5+n6+n7+n8+n9
dvd = str(dv1/11)
seldv1 = (int(dvd[3:4])+1)
sub1 = int()
if seldv1 >= 2:
    sub1 = 11
else:
    sub1 = 0
resto1 = sub1-seldv1
#Digito 2
dv2 = nd1+nd2+nd3+nd4+nd5+nd6+nd7+nd8+nd9+(resto1*2)
dvd2 = str(dv2/11)
seldv2 = (int(dvd2[3:4])+1)
#Verifica as condições para subtração
sub2 = int()
if seldv2 >= 2:
    sub2 = 11
else:
    sub2 = 0
resto2 = sub2-seldv2
if resto1 == 10:
    resto1 = 0
if resto2 == 10:
    resto1 = 0
#Verifica se o CPF está no formato correto.
if((resto1 == d10) and (resto2 == d11)):
    print('CPF VALIDADO!')
else:
    print('CPF INVALIDO!')
