consumo = float(input('digite seu consumo em kWh: '))
valorkWh = float(input('digite o valor do kWh cobrado: '))

fatura= float(consumo * valorkWh)
print('O valor da fatura é R$%.2f' %fatura)
