# calculando média  if elif
print(' ')
n1 = float(input(' Qual a primeira nota? '))
n2 = float(input(' Qual a segunda nota? '))
med = (n1 + n2) / 2
print(' ')
if med < 5:
    print(' Média abaixo de 5,0 -> REPROVAÇÃO ')
    print(' Sua média final foi apenas {}'.format(med))
elif med >= 5 and med <= 6.9:
    print(' Média entre 5 e 6,9 -> RECUPERAÇÂO')
    print(' Sua média final foi de {} ESTUDE MAIS!'.format(med))
elif med >= 7:
    print(' Média 7,0 ou superior -> APROVAÇÃO')
    print(' Sua média final foi {}'.format(med))