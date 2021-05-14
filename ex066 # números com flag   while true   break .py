# números com flag   while true   break

soma = cont = 0
while True:
    num = int(input('[Pare digitando 999] Digite um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
#print('Você digitou {} números e a soma entre eles foi {}.'.format(cont, soma))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}.')