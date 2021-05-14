#PA soma de 10 termos (n termo da PA)  for

print(' ')
primeiro = int(input(('Primeiro termo:  ')))
razao = int(input('Razão '))
decimo = primeiro + (10 - 1 ) * razao #(enésimo termo da PA)
for c in range(primeiro,decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')