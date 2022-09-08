a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero: "))

if a > b and a > c:
    print('o maior numero é',a,)
if b > a and b > c:
    print('o maior numero é',b,)
if c > a and c > b:
    print('o maior numero é',c,)
if a == b and b==c :
    print('os numeros sao iguais')
if a < b and a < c:
    print('o menor numero é', a,)
if b < a and b < c:
    print('o menor numero é', b,)
if c < a and c < b:
    print('o menor numero é',c,)
if a!=b and b!=c and c!=a:
    print('são todos diferentes')
