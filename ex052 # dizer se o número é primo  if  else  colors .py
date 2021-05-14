#Dizer se o número é primo  if  else  colors
print(' ')
num = int(input('Digite um númro: '))
total = 0
print(' ')
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\033[m O número {} foi divisível {} vezes'.format(num,total))
if total == 2:
    print(('E por isso ele é PRIMO!'))
else:
    print(('E por isso ele NÃO É PRIMO.'))