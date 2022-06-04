n = 0
s = 0 
nd = 0
resp = 's'

while resp == 's' or resp == 'S':
    n = int(input('Digite um número: '))
    s += n
    nd += 1
    while resp != 's' or resp != 'S' or resp != 'n' or resp != 'N':
        resp = str(input('Deseja continuar? [S/N]: '))
        if resp == 'S' or resp == 's':
            break
        elif resp == 'N' or resp =='n':
            break
        else:
            print('Opção inválida. Tente novamente')
            continue
print(f'Ao todo foram digitados {nd} números e a soma entre eles é {s}')
