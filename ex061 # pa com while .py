#PA com while

print(' ')
print('Gerador de PA. Escreva abaixo! ')
print(' ')
primeiro = int(input(('Primeiro termo: ')))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{}'.format(termo), end='-> ')
    termo += razao
    cont += 1
print('ACABOU')