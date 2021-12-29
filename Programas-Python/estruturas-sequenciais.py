salario_mensal = float(input('\033[1;97mDigite o seu salário mensal: '))
gasto_mensal = float(input('Digite em média o seu gasto mensal: \033[m'))

salario_anual = salario_mensal * 12
gasto_anual = gasto_mensal * 12

economia_anual = salario_anual - gasto_anual
print(f'\033[1;97mO valor economizado ao final do ano será de:R${economia_anual:.2f}\033[m')
