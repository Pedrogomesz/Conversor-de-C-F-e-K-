print('-------------Conversor de CFK---------------')
print('--------------------------------------------')

print('Escolha a sua Operação: \n (1) Celsius -> Fahrenheit \n (2) Fahrenheit -> Celsius \n (3) Celsius -> Kelvin \n (4) Kelvin -> Celsius')
print('Se Não tiver qualquer dado pode colocar x no lugar')

op = input('Escreva sua operação: ')

match op:
    case '1':
        c = float(input('Escreva o valor de celsius: '))
        f = c*1.8+32
        print(f'Resultado do seu Fahrenheit °{f}')
    case '2':
        f = float(input('Escreva o valor de Fahrenheit: '))
        c = (f-32)/1.8
        print(f'Resultado do seu Celsius °{c}')
    case '3':
        c = float(input('Escreva o valor de Celsius: '))
        k = c+273
        print(f'Resultado do seu Kelvin °{k}')
    case '4':
        k = float(input('Escreva o valor de Kelvin: '))
        c = k-273.15
    case _:
        print('Operação não encontrada!')