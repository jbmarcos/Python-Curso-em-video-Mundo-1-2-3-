# Par ou Ímpar    while true   -=-

from random import randint
from time import sleep

cont=0
P = 2
I = 1
print('')
print('<< PAR ou ÍMPAR? >>     Jogue contra o Robozino Chico -->   (⊙ˍ⊙) oi')
print('')
while True:
    bot = randint(1,2)
    n = int(input('Escolha: [\033[35m2\033[m para PAR ou \033[34m1\033[m para ÍMPAR] '))
    print('')
    if n == 1 and bot == 2:
        print('Você jogou 1, Chico 2. 1+2=\033[33m 3\033[m é ÍMPAR. Você Ganhou!')
        cont += 1
        sleep(2)
        print('')
    elif n == 1 and bot==1:
        print('Você jogou 1, Chico 1. 1+1=\033[33m 2\033[m é PAR. Você \033[31mPerdeu!\033[m')
        break

    elif n == 2 and bot==2:
        print('Você jogou 1, Chico 1. 1+1=\033[33m 2\033[m é PAR. Você Ganhou!')
        cont += 1
        sleep(2)
        print('')
    elif n == 2 and bot==1:
        print('Você jogou 2, Chico 2. 2+1=\033[33m 3\033[m é ÍMPAR. Você \033[31mPerdeu!\033[m')
        break

if cont == 1:
    print(f'GAME OVER. Você venceu {cont} vez!')
else:
    print(f'GAME OVER. Você venceu {cont} vezes!')



'''
from random import randint
print('-' * 30)
print(f'{" Par ou Ímpar ":~^30}')
print('-' * 30)

acumulador = 0
while True:
    jogador = int(input('\nInforme um valor: '))
    parOrImpar = input('Deseja PAR ou ÍMPAR ? [P/I] ').strip().upper()
    print('-' * 30)
    computador = randint(0, 10)

    while parOrImpar != 'P' and parOrImpar != 'I':
        print('Informe corretamente qual deseja.')
        parOrImpar = input('Deseja PAR ou ÍMPAR ? [P/I] ').strip().upper()
        print('-' * 30)

    resulValor = jogador + computador

    print(f'Você jogou: {jogador}\nComputador jogou: {computador}\n{jogador} + {computador} = {jogador + computador}')

    if resulValor % 2 == 0:
        print('Resultado: Deu PAR')
        if parOrImpar == 'P':
            print('\nVocê Acertou!!!')
            print('Mais uma rodada...')
            acumulador += 1
        else:
            print('\nVocê Perdeu!!!')
            break
    else:
        print('Resultado: Deu ÍMPAR')
        if parOrImpar == 'I':
            print('\nVocê Acertou!!!')
            print('Mais uma rodada...')
            acumulador += 1
        else:
            print('\nVocê Perdeu!!!')
            break
    print('-' * 30)

print('-' * 30)
print('FIM DE JOGO!!!')
print('-' * 30)
print(f'Você teve {acumulador} vitória(s) consecutiva(s)')'''

