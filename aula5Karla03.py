'''Fazer um programa para imprimir a soma das linhas das matrizes e a soma total dos  elementos PARES da matriz.'''

m=[]
l=3
c=3
somaL=somaP=0

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
        somaL+=m[i][j]
        if m[i][j]%2==0:
            somaP+=m[i][j]


print('\n\nSoma dos pares: {:1d}'.format(somaP))
print('\n\nSoma das linhas: {:1d}'.format(somaL))
