kwh = int(input('Quantidade de kWh consumida: '))
tipo = input('Tipo de instalação: ')
conta = 0

if tipo == 'R' or tipo == 'r':
    print('RESIDENCIAL')
    if kwh <= 500:
        conta = kwh * 0.40
        print(conta)
    elif kwh > 500:
        conta = kwh * 0.65
        print(conta)
else:
    if tipo == 'C' or tipo == 'c':
        print('COMERCIAL')
        if kwh <= 1000:
            conta = kwh * 0.55
            print(conta)
        elif kwh > 1000:
            conta = kwh * 0.60
            print(conta)
    else:
        if tipo == 'I' or tipo == 'i':
            print('INDUSTRIAL')
            if kwh <= 5000:
                conta = kwh * 0.57
                print(conta)
            elif kwh > 5000:
                conta = kwh * 0.68
                print(conta)
        else:
            print('Tipo invalido')
