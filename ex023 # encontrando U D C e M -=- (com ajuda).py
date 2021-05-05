# encontrando U D C e M -=- (com ajuda)

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))


"""esse abaixo tb funcionou mas n entendi como
n = int(input('Digite um número entre 0 e 9999:'))
ns = ('{:4}'.format(n))
nss = str(ns.replace(' ','0'))
print('''Pelo metodo de manipulação de string:
Número {}
Milhares:  {}
Centenas:  {}
Dezenas:  {}
Unidades:  {}'''.format(nss, nss[0], nss[1], nss[2], nss[3]))'''"""
