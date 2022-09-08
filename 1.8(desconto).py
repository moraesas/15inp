import sys
v_mercadoria = float(sys.argv[1])
p_desconto = float(sys.argv[2])

desconto = p_desconto / 100
total = v_mercadoria * desconto
valort= v_mercadoria - total

print('valor da mercadoria : %.2f' %v_mercadoria)
print('percentual de desconto : %.2f' %desconto)
print('valor de desconto em R$%.2f' %total)
print('total a pagar em R$%.2f' %valort)
