# JO KEN POO   '''  if  elif
from random import randint
from time import sleep

bot = randint(0,2)
print(' ')
print('JO KEN PÔ... Vamos jogar!')
print(' ')
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
print(' ')
jogador = int(input('Qual a sua jogada? '))
print(' ')
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('pô')
sleep(1)
print(' ')
itens = ('Pedra', 'Papel','Tesoura')
print('O computador jogou {}'.format(itens[bot]))
print('Você jogou {}'.format(itens[jogador]))

if bot == 0: #pedra
    if jogador == 0:
        print('--> Empate! <--')
    elif jogador == 1:
        print('--> Você venceu! ✅')
    elif jogador == 2:
        print('--> O computador venceu! <@_@>')
    else:
        print('Jogada inválida!')

elif bot == 1: #papel
    if jogador == 0:
        print('--> O computador venceu! <@_@>')
    elif jogador == 1:
        print('--> Empate! <--')
    elif jogador == 2:
        print('--> Você venceu! ✅')
    else:
        print('Jogada inválida!')

elif bot == 2: #tesoura
    if jogador == 0:
        print('--> Você venceu! ✅')
    elif jogador == 1:
        print('--> O computador venceu! <@_@>')
    elif jogador == 2:
        print('--> Empate! <--')
    else:
        print('Jogada inválida!')