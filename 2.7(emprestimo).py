# emprestimo bancario
valorcasa = float(input('Valor da casa que deseja comprar: '))
salario = float(input('Salario atual: '))
anos = int(input('Anos a pagar: '))


meses = anos * 12
prestacao = float(valorcasa / meses)
sal = salario * 0.3


if prestacao > sal:
    print('NEGADO!\nO valor da parcela excede 30% do salario')
else:
    print('APROVADO!\nO valor da parcela é de R$%.2f' %prestacao)
