# encontra primeiro e último termo -=- split

n1 = str(input('Digite seu nome completo: ')).strip()
n2 = n1.split()
print('Pazer em te conhecer!')
print('Seu primeiro nome é {}'.format(n2[0]))
print('O seu último nome é {}'.format(n2[len(n2)-1]))
