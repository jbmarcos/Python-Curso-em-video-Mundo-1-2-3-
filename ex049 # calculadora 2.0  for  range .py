# calculadora 2.0  for  range
print(' ')
num = int(input('Digite um número para cer sua tabuada: '))
print(' ')
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))