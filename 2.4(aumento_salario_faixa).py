salario = float(input('Digite seu salário: '))
aumento = 0
if salario <= 1250:
    aumento= salario * (15/100)
    salario = float(salario + aumento)
    print('O aumento foi de R$',aumento, ' novo salário é de R$%.2f' %salario)


else:
    aumento = salario * (10/100)
    salario = float(salario + aumento)
    print('O aumento foi de RS',aumento,'novo salário é de R$%.2f' %salario)
