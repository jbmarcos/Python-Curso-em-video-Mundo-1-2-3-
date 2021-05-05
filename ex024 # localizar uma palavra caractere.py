# localizar uma palavra/caractere

nome = str(input('Digite o nome da sua cidade: ')).strip()
#print('Santo'in nome)
print(nome[:5].upper() == 'SANTO')