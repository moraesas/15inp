import sys
dias = int(sys.argv[1])
horas = int(sys.argv[2])
minutos = int(sys.argv[3])
segundos = int(sys.argv[4])


# 1 dia = 24h
# 24h = 86400
# 1h = 3600
# 1 minuto = 60

dias = dias * 24
horas = horas * 3600
minutos = minutos * 60

total = dias + horas + minutos + segundos

print('o total em segundos do usuario é %.2f' %total)
