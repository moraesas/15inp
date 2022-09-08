velocidade = float(input('Qual a velocidade do carro: '))
multa = 0
if velocidade > 80:
    multa = velocidade - 80
    valor = float(multa * 30)
    print('Você foi multado, o valor cobrado é de R$%.2f\nDevagar na proxima!!!' %valor)
elif velocidade == 80:
    print('Velocidade máxima permitida')
elif velocidade < 60:
    print('Acelera esse carro parcero')
else:
    print('Parabéns, você é bom motorista')
