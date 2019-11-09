'''Fazer um programa para guardar a soma dos elementos da diagonal
principal de uma matriz 3x3 mais a soma dos elementos da diagonal
secundária de uma outra matriz 3x3 em um vetor.'''

m1=[]
m2=[]
l=3
c=3

for i in range(0, l):
    m1=[None]*l
    m2=[None]*l
    for j in range(0, c):
        m1[j]=[None]*c
        m2[j]=[None]*c

for i in range(0, l):
    for j in range(0, c):
        m1[i][j]=float(input('Digite um número para M1: '))

print()

for i in range(0, l):
    for j in range(0, c):
        m2[i][j]=float(input('Digite um número para M2: '))

print('\nMATRIZ 1:')
for i in range(0, l):
    print()
    for j in range(0, c):
        print(m1[i][j], end='  ')

print('\n\nMATRIZ 2:')
for i in range(0, l):
    print()
    for j in range(0, c):
        print(m2[i][j], end='  ')

soma1=0
soma2=0
soma=[]

for i in range(0, 3):
    for j in range(0, c):
        if i==j:
            soma1+=m1[i][i]
            soma2+=m2[3-1-i][i]

soma.append(soma1)
soma.append(soma2)

print('\n\nDIAGONAIS:')
print(soma)


