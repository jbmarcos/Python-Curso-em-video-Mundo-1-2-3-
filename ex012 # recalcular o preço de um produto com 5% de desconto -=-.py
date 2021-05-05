# recalcular o preço de um produto com 5% de desconto -=-

valor1 = float( input( 'Qual o valor do produto? R$'))
desc = valor1 * 5 / 100
valor2 = valor1 - desc
print( 'O novo valor do produto com 5% de desconto é de: ',valor2 , 'R$.')