# encontra seno cosseno tangente de um número -=-

import math
num = float(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(num))
cos = math.cos(math.radians(num))
tan = math.tan(math.radians(num))
print('O ângulo de {} tem o SENO de {:.2f}'.format(num, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(num, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}' .format(num, tan))
