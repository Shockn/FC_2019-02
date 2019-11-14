'''Fazer um programa que encontre o produto dos números ímpares positivos menores do que N, 
inclusive:'''

def prodImpar(n):
    if n==1:
        return(1)
    else:
        return(n*prodImpar(n-2))

try:
    x=int(input('Digite um número: '))
    print('O produto dos n valores são: {:1d}.'.format(prodImpar(x)))
except:
    print('Valor inválido.')