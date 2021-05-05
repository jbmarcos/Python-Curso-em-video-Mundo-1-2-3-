# verifica a velocidade do carro, gera multa  -=- if: condição simples

velo = float(input('Qual a velocidade do carro agora? '))
if velo > 80:
    print('Você foi multado. Excedeu a vellocidade de 80 Km/H')
    multa = (velo-80) * 7
    print('Você deve pagar uma multa de Rs{:.2f}!'.format(multa))
print('Muito bem. Sua velocidade está dentro dos limites. Dirija com segurança!!')