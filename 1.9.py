km = float(input('Distância a percorrer em km: '))
velocidade_m = float(input('Velocidade média esperada para a viagem: '))

tempo = km / velocidade_m

print('O tempo médio de viagem para uma viagem de ',km,'km é de %1.f horas' %tempo)