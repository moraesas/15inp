salario = float(input("Digite o valor do salário minimo atual: "))
kw = float(input("Digite a quantidade de Kw consumida na residência: "))

valorkw = salario / 5
valorconta = valorkw * kw
total = float((valorconta * 0.85))


print('o Valor do Kw em 2022 é R$',valorkw,)
print('o valor da conta de luz nessa residência é R$',valorconta,)
print('o valor da conta com desconto é de R$%.1f' %total)
