'''Fazer um programa para ler os dados para uma matriz 3x3 e somar os elementos (valores) PARES da matriz.'''

m=[]
l=3
c=3
soma=0

for i in range(0, l):
    m=[None]*l
    for j in range(0, c):
        m[j]=[None]*c

for i in range(0, l):
    for j in range(0, c):
        m[i][j]=int(input('Digite um número para o elemento[{:1d}][{:1d}]: '.format(i, j)))

print('\nMATRIZ: ')
for i in range(0, l):
    print()
    for j in range(0, c):
        print(m[i][j], end='  ')
        if m[i][j]%2==0:
            soma+=m[i][j]

print('\n\nSoma dos elementos pares: {:1d}'.format(soma))
