p_numero = int(input('Digite um numero: '))
s_numero = int(input('Digite um numero: '))

if p_numero > s_numero or p_numero >= s_numero:
    print('O primeiro número é maior ou maior igual que o segundo número')
elif p_numero == s_numero:
    print('O primeiro número é igual ao segundo número')
elif s_numero > p_numero or s_numero >= p_numero:
    print('O segundo número é maior ou maior igual que o primeiro número')
elif s_numero != p_numero:
    print('O segundo numero é diferente do primeiro número')
