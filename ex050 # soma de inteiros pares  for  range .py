#soma de inteiros pares  for  range

soma = 0
cont = 0
print(' ')
for c in range(1, 7):
    num = int(input('Digite o {} valor. '.format(c)))
    if num % 2 == 0:
        soma = soma + num #soma +=1
        cont = cont + 1 #cont += 1
print(' ')
print('Você infotmou {} números PARES e a SOMA foi {}'.format(cont, soma))