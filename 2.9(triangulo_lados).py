import sys
reta1 = sys.argv[1]
reta2 = sys.argv[2]
reta3 = sys.argv[3]

if reta1 + reta2 < reta3 or reta2 + reta3 < reta1 or reta3 + reta1 < reta2:
    print('valores invalidos')
else:
    print('triangulo')
