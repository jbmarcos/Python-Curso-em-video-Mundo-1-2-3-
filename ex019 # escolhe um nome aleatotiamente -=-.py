# escolhe um nome aleatotiamente -=-

import random
n1 = input('Escreva o nome. Primeiro aluno: ')
n2 = input('Escreva o nome. Segundo aluno: ')
n3 = input('Escreva o nome. Terceiro aluno: ')
n4 = input('Escreva o nome. Primeiro aluno: ')
lista = [n1, n2, n3,n4]
n = random.choice(lista)
print('O aluno ecolhido foi', n )
