valor_onibus = 4.40
valor_uber = float(input('Digite o valor da corrida: '))

if valor_uber <= valor_onibus * 5:
    print('Pegue a corrida')
elif valor_uber <= valor_onibus *6:
    print('Espere um pouco, pois o valor pode abaixar')
else:
    print('Pegue o ônibus')
