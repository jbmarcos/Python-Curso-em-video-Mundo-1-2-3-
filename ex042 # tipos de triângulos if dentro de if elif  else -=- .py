# tipos de triângulos if dentro de if elif  else -=-

print(('Ecolha valores para formar um triângulo!'))
print(' ')
v1 = int(input('\033[1;30;43m Valor 1: '))
v2 = int(input('\033[1;30;41m Valor 2: '))
v3 = int(input('\033[1;30;42m Valor 3: \033[m'))
print(' ')
if v1<v2+v3 and v2<v1+v3 and v3<v1+v2:
    print('\033[1;32;40m ✅✅✅  Esses valores formam um triangulo \033[m', end='')
    if v1 == v2 == v3:
        print(' EQUILÁTERO')
    elif v1 != v2 != v3 != v1:
        print(' ESCALENO')
    else:
        print(' ISÓECELES')

else:
    print('\033[1;31;40m Esses valores não podem formar um triangulo ❎❎❎ \033[m')