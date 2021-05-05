# porcentagens multiplas

valor = float(input('Qual o valor do salário? '))
if valor <= 1250:
    novo = valor + (valor*15/100)
else:
    novo = valor + (valor*10/100)
print('O salário era {:.2f} e aumentou para {:2.2f}'.format(valor, novo))