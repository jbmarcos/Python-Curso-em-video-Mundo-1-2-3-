# jogo random number  while not randint  if elif else

from random import randint
pc = randint(0,10)
print('Sou seu computador. Pensei em um número de 0 a 10. Será que você consegue adivinhar qual foi???')
certo = False
palpite = 0
while not certo:
    player = int(input('Qual seu palpite? '))
    palpite = palpite + 1
    if player == pc:
        certo = True
    else:
        if player < pc:
            print('Mais...Tente novamente')
        elif player > pc:
            print('Menos...Tente novamente')
print('Acertou na tentativa {}. PARABÉNS!'.format(palpite))