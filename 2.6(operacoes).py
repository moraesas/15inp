a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))

print('(+) soma\n(-) subtração\n(*) multiplicação\n(/) divisao\n')
op = input('Qual operação deseja realizar? ')
ope = 0
if op == '+':
    ope = a + b
    print('O resultado da soma é:%s' %ope)
elif op == '-':
    ope = a - b
    print('O resultado da subtração é:%s' %ope)
elif op == '*':
    ope = a * b
    print('O resultado da multiplicação é:%s ' %ope)
elif op == '/':
    ope = a // b
    print('O resultado da divisão é:%s' %ope)
elif op != '+''-''*''/':
    print('operação inválida')
else:
    print('Numero invalido')
