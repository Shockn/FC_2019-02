'''Crie um algoritmo que leia um número N e imprima se ele é perfeito ou não. Um número é perfeito quando a 
soma dos seus divisores é igual a ele mesmo, e.g., 6 = 3 + 2 + 1.'''

def perfeito(x):
    total=0
    for i in range(1, n):
        if x%i==0:
            total+=i
    if total==x:
        return('{:1d} é um número perfeito.'.format(x))
    else:
        return('{:1d} não é um número perfeito.'.format(x))

n=int(input('Digite um número: '))
print(perfeito(n))
