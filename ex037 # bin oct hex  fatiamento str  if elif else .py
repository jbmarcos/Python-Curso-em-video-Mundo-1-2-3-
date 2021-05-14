# bin oct hex  fatiamento str  if elif else

num = int(input(' Digite um númeto inteiro: '))
print('''Escolha a base de conversção que deseja: 
[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal''')
opção = int(input(' Sua opção: '))
if opção == 1:
    print(' {} convertido para Binário é {} '.format(num, bin(num) [2:]))
elif opção == 2:
    print(' {} convertido para Octal é {}'.format(opção, oct(num) [2:]))
elif opção == 3:
    print(' {} convertido para Hexadecimal é {}'.format(opção, hex(num) [2:]))
else:
    print(' Opção inválida. Tente novamente.')