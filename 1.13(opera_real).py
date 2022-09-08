import sys

n = (float(sys.argv[1]))

inteiro = int(n)
fracionaria = n - inteiro

a = ' a parte inteira é: %1.f\n' %inteiro
b = ' a parte fracionaria é: %.5f\n' %fracionaria
c = ' numero arredondado decimal: %.1f\n' %n
d = ' numero arredondado inteiro: %1.f ' %n

resposta = a + b + c + d

print(resposta)
