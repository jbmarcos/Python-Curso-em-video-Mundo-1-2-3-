#Menores ou maiores de idade   for  if  else
print('')
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('')
print('No total tivemos {} maiores de idade e {} menores de idade.'.format(totmaior, totmenor))