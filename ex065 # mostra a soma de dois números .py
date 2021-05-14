resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digitr um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            maior = num
    resp = str(input('Continuar? [S/N] ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} números e a média entre eles foi de {}. '.format(quant, media))