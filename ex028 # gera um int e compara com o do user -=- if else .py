# gera um int e compara com o do user -=- if: else:

from random import randint
import time
print('---'*25)
print('---'*25)
n1 = int(input('\033[30;44m Tente adivinhar qual número vou escolher. Digite um número de 1 a 5: ' ))
print('---'*25)
print('---'*25)
print('Pensando... ... ...')
print('---'*25)
print('---'*25)
n2 = (randint(1,5))
time.sleep(3)
if n1 == n2:
    print('\033[30;42mParabéns você acertou, o número foi {}!!!' .format(n1))

else:
    print('\033[1;30;41m A,que pena. Vovê errou. O número foi {}. Tente outra vez!!'.format(n2))