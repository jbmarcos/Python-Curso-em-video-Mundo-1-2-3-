# categoria na natação  if elif else -=-

from datetime import date
atual = date.today().year
print(' ')
nasc = int(input(' Qual o ano de nascimento do atleta? '))
print(' ')
idade = atual - nasc
print(' Com {} anos de idade,'.format(idade))
if idade <=9:
    print(' o atleta é da categoria MIRIM. ')
elif idade <= 14:
    print(' o atleta é da categoria INFANTIL.')
elif idade <= 19:
    print(' o atleta é da categoria JÚNIOR.')
elif idade <= 25:
    print(' o atleta é da categoria SÊNIOR.')
elif idade >26:
    print(' o atleta é da categoria MASTER.')