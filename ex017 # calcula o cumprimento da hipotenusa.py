# calcula o cumprimento da hipotenusa

'''opo = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hip = (opo ** 2 + adj ** 2) ** (1/2)
print('O cumprimento da hipotenusa é: {:.2f} '.format(hip))'''

import math
opo = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hip = math.hypot(opo, adj)
print('O cumprimento da hipotenusa é: {:.2f} '.format(hip))