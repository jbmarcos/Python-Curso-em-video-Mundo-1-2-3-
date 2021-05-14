# fatorial   while

num = int(input("Digite um número: "))
cont = num
fact = 1
while cont>0:
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fact = fact * cont # fact *= cont
    cont = cont - 1 #cont -= 1
print('\033[34m{}\033[m'.format(fact))

'''from math import factorial
num = int(input("Digite um número: "))
fat = factorial(num)
print('O Fatorias de {} é \033[33m{}\033[m.'.format(num, fat))'''