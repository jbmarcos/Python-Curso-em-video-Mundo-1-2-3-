# imc  if elif

print(' ')
pe = float(input('Qual é o seu peso? (Kg) '))
al = float(input('Qual sua altura? (m) '))
imc = pe/(al ** 2)
print(' ')
print(' O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print(' Você está ABAIXO do peso normal.')
elif 18.5 <= imc < 25:
    print(' PARABÉNS!!! Você está na faixa de peso ADEQUADO.')
elif 25 <= imc < 30:
    print(' Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print(' Você está em OBESIDADE.')
elif imc >= 40:
    print(' Você está em OBESIDADE MORBIDA, cuidado!!!')
