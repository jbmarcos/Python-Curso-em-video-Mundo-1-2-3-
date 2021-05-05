# procurar por caracteres ordinalmente -=-

nome = str(input("Didite uma frase: ")).upper().strip()
print('A letra A apatece {} vezes na frase.'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {}'.format(nome.rfind('A')+1))
