#palíndromo  split  join  upper  strip  if

print(' ')
print('-='*20)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto =''.join(palavras)
inverso = junto[::-1]
print('-='*20)
print(' ')
print('O inverso de {} é {}'.format(junto, inverso))
print(' ')
if inverso == junto:
    print('O que você digitou é um PAlÍNDROMO!')
else:
    print('O que você digitou NÃO é um PAlÍNDROMO!')