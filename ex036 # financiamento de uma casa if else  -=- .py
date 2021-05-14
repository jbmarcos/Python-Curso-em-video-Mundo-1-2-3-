# financiamento de uma casa if else  -=-

print(' ')
casa = float(input(' Valor da casa: R$ '))
ganha = float(input(' Qual o valor mensal ganho pelo comprador? '))
anos = int(input(' Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
print(' ')
print(' Para pagar uma casa de {:.2f} R$'.format(casa))
print(' A prestação será de {:.2f} reais mensais.'.format(prestacao))
print(' ')
minimo = ganha * 30 /100

if prestacao <= minimo:
    print(' Parabéns. Emprestimo CONCEDIDO')
else:
    print(' Empréstimo NEGADO')
