# valores extremos min e max  for  if

print('')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}ª   pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('')
print('O maior peso foi {} Kg e o menor foi {} Kg.'.format(maior, menor))