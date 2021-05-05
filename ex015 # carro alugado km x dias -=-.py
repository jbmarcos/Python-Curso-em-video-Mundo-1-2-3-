# Carro alugado km x dias -=-

km = float(input('Quantos Km foram percorridos? '))
dias = int(input('O carro foi alugado por quantos dias? ' ))
pagar = dias * 60 + km * 0.15
print('O valor a ser pago pelo uso do carro é de: {:.2f} R$' .format(pagar))