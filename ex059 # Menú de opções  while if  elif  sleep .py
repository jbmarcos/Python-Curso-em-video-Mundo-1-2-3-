# Menú de opções  while if  elif  sleep

from time import sleep
print('')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior valor
    [4] novos números
    [5] sair do programa
    ''')
    opção = int(input('>>> Qual sua opção? '))
    if opção == 1:
        soma = n1 + n2
        sleep(1)
        print('A soma rente {} e {} é exatamente \033[31m{}\033[m.'.format(n1, n2, soma))
        sleep(3)
    elif opção == 2:
        multiplic = n1 * n2
        sleep(0.5)
        print('A multiplicação entre {} e {} é \033[31m{}\033[m.'.format(n1, n2, multiplic))
        sleep(3)
    elif opção == 3:
        if n1>n2:
            sleep(0.5)
            print('O maior valor é \033[31m{}\033[m.'.format(n1))
        elif n2>n1:
            sleep(0.5)
            print('O maior valor é \033[31m{}\033[m.'.format(n2))
        elif n1 == n2:
            sleep(0.5)
            print('Opa, os valores são iguais!')
        sleep(3)
    elif opção == 4:
        sleep(0.5)
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(3)
    elif opção == 5:
        sleep(0.5)
        print('\033[31mSaindo...\033[m')
        sleep(1)
    else:
        print('Opção inválida, tente novamente! ')
print('Fim do programa. Volte sempre!')