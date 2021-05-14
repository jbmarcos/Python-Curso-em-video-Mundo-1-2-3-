# loja baratão  tratando dados  while True  if  break

total = mil = menor = quant = 0
barato = ''
print(' ')
print('~~~~~~~~~~~~~~~~~~~~ LOJA SUPER BARATÃO ~~~~~~~~~~~~~~~~~~~~')
while True:
    print(' ')
    nome = str(input('Qual o nome do produto? '))
    preco = int(input('Qual o preço do produto? R$ '))
    quant = quant + 1
    if quant == 1:
        menor = preco
        barato = nome
    if preco < menor:
        menor = preco
        barato = nome

    total = total + preco
    if preco >= 1000:
        mil = mil + 1
    res = str(input('Deseja continuar? [S/N]: ')).upper()
    while res not in 'N' and res not in 'S':
        res = str(input('Responda com sim ou nao [S/N]: ')).upper()
    if res == 'N':
        break
print(' ')
print('~~~~~~~~~~~~~~~~~~~~ Compra finalizada ~~~~~~~~~~~~~~~~~~~~')
print(' ')
print(f'O total da compra deu: R$ {total},00')
print(f'A quantidade de produtos que custam mais de mil reais é: {mil}')
print(f'O produto de menor valor foi {barato} e custou R$ {menor},00.')
print(' ')
print('~~~~~~~~ AGRADECEMOS POR SUA COMPRA. VOLTE SEMPRE! ~~~~~~~~')