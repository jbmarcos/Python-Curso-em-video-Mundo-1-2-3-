#Questionário 4 pessoas, 3 perguntas  soma  media  nome  if  for
somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

print('')
for p in range(1,5):
    print('----- {}ª PESSOA ----- '.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('')
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1 #totmulher20 += 1

médiaidade = somaidade / 4
print('Os resultados são:')
print('--> A média de idade do grupo é de {} anos.'.format(médiaidade))
print('--> O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('--> Ao todo são {} mulhere(s) com menos de 20 anos.'.format(totmulher20))