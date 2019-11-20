'''Fazer um programa que encontre o produto dos números ímpares positivos menores do que N, 
inclusive:'''

def prodImpar(n):
    if n==1:
        return(1)
    else:
        return((n-2)*prodImpar(n-2))

try:
    num=int(input('Digite um número impar: '))
    print('O produto dos número impares menores que N é: {:1d}'.format(prodImpar(num)))
except:
    print('Número inválido.')
