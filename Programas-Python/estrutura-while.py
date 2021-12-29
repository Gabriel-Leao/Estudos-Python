n = 0
s = 0 
nd = 0

while True:
    n = int(input('Digite um número: '))
    s += n
    nd += 1
    resp = str(input('Deseja continuar? [S/N]'))
    if resp == 'S' or resp == 's':
        continue
    elif resp == 'N' or resp =='n':
        break
print(f'Ao todo foram digitados {nd} números e a soma entre eles é {s}')
