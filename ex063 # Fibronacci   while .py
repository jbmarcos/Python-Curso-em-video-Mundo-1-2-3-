# Fibronacci   while <=


n = int(input('Quantos valores quer ver dentro da sequência de Fibroonacci? '))
v1 = 0
v2 = 1
print('{}-> {}'.format(v1, v2), end='')
cont = 3
while cont <= n:
    v3 = v1 + v2
    print('-> {}'.format(v3))#, end='')
    v1 = v2
    v2 = v3
    cont += 1
print('-> FIM')