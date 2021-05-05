# par ou impar ? if: else:

num = int(input('Digite um nímero: '))
resultado = num % 2
if resultado == 0:
    print(' O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR'.format(num))