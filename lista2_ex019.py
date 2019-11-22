'''Crie um algoritmo que leia um número N e imprima os N primeiros números primos. O seu programa 
deve fazer o MÍNIMO de interações possíveis.'''

n=int(input('Digite um número: '))
l=[]

for i in range(2, n+1):
    primo=True
    for j in range(2, i):
        if i%j==0:
            primo=False
        else:
            pass
    if primo==True:
        l.append(i)

print('\nNúmeros primos até {:1d}:'.format(n))
for i in range(len(l)):
    print(l[i], end=' ')