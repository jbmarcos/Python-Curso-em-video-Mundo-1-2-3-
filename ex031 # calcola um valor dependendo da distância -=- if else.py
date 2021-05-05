# calcola um valor dependendo da distância -=- if: else:

dist = float(input('Sua viagem é de quantos Km ? '))
print('Para sua viagem de {}Km'.format(dist))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('O valor da sua passagem é de R$ {:.2f}'.format(valor))