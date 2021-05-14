# simulador de loja    if  elif  else
print(' ')
rs = float(input('Qual o valor das compras? R$ = '))
print(' ')
print('''Formas de pagamento
[ 1 ] à vista dinheiro/déboto/PIX
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais vezes no cartão''')
print(' ')
opção = int(input('Qual a opção? '))
if opção == 1 :
    total = rs - (rs * 10 / 100)
    print('Sua compra de {} R$ vai custar {} no final com desconto de 10%. '.format(rs, total))
elif opção == 2:
    total = rs - (rs * 5 / 100)
    print('Sua compra de {} R$ vai custar {} no final com desconto de 5%. '.format(rs, total))
elif opção == 3:
    total = rs / 2
    print('Sua compra será parcelada em 2x de {} R$.'.format(total))
    print('A compra de {} R$ custará no final o mesmo valor de {} R$.'.format(rs, rs))
elif opção == 4:
    total = rs + (rs * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    totalPorParcela = rs / parcelas
    print(' ')
    print('Sua compra será parcelada em {}x de {} R$.'.format(parcelas, totalPorParcela))
    print('A compra de {} R$ custará no final com 20% de juros o valor de {} R$.'.format(rs, total))
else:
    print(' ')
    print('Opção incorrerta. Tente novamente.')



