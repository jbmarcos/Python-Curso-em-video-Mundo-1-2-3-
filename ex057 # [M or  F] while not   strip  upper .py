# [M / F] while not   strip  upper

sexo = str(input('Digite seu sexo: [M/F] ')) .strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe corretamente: ')).strip().upper()[0]
print(sexo)