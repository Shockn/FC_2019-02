'''Fazer um programa recursivo para calcular x^y através de multiplicações sucessivas'''

def potenciacao(x, y):
    if y==0:
        return(1)
    else:
        return(x*potenciacao(x, y-1))

try:
    base=float(input('Digite a base: '))
    expoente=int(input('Digite um expoente: '))
    print('{:1.2f} ^ {:1d} = {:1.2f}'.format(base, expoente, potenciacao(base, expoente)))
except:
    print('Número inválido.')