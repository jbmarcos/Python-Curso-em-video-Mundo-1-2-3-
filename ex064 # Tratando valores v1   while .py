# Tratando valores v1   while

num = cont = soma = 0
while num != 999:
    num = int(input('[Pare digitando 999] Digite um número: '))
    soma += num
    cont += 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont-1, soma-999))


'''num = cont = soma = 0
num = int(input('[Pare digitando 999] Digite um número: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('[Pare digitando 999] Digite um número: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))'''
