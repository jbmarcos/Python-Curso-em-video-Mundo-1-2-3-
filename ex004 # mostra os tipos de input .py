# mostra os tipos de input -=-

a = input ('Escreva algo:')
print ('As informações sobre o que vc digitou são as seguintes:')
print('Só tem espaços? ', a.isspace())
print('É alfabético?', a.isalpha())
print('É um númro?', a.isnumeric())
print('É alfanumerico?', a.isalnum())
print('Está maiuscula?', a.isupper())
print('Está em minuscula?', a.islower())
print('Está capitalizada?,', a.istitle())

