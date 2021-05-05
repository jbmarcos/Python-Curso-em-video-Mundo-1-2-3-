# cria uma sequencia aleatotiamente -=-

import random
n1 = input('Escreva o nome. Primeiro aluno: ')
n2 = input('Escreva o nome. Segundo aluno: ')
n3 = input('Escreva o nome. Terceiro aluno: ')
n4 = input('Escreva o nome. Primeiro aluno: ')
lista = [n1, n2, n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
