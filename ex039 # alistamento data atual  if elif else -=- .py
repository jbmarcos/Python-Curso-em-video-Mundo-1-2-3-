# alistamento data atual  if elif else -=-

from datetime import date
atual = date.today().year
print(' ')
nasc = int(input(' Qual o ano de nascimento? '))
idade = atual - nasc
print(' ')
print(' Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
print(' ')
if idade < 18:
    print(' Ainda faltam {} anos para o alistamento.'.format(18 - idade ))
    print(' O alistamento será em {}.'.format(nasc + 18))
elif idade > 18:
    print(' O alistamento deveria ter acontecido a {} anos.'.format(idade - 18))
    print(' O ano de alistamento foi em {}.'.format(nasc + 18))
else:
    print(' O alistamento deve ocorrer IMEDIATAMENTE!')
