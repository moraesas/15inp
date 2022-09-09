distancia = float(input('Quantos km deseja percorrer: '))
passagem = 0

if distancia < 200:
    passagem = distancia * 0.50
    print('O valor da passagem para %.2f km é R$' %distancia,passagem,)
else:
    passagem = distancia * 0.45
    print('O valor da passagem para %.2f km é de R$' %distancia,passagem,)
