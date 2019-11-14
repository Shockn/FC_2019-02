'''Escrever um programa para ler dois números e imprimir a sua divisão.'''

try:
    x=float(input('Digite o dividendo: '))
    y=float(input('Digite o divisor: '))
    try:
        z=x/y
        print(z)
    except:
        print('\nDivisão inválida.')
except:
    print('\nValor inválido.')