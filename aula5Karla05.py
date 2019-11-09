'''Fazer um programa para guardar os elementos
de uma matriz 4x5 em um vetor'''

m=[]
v=[]
l=4
c=5

for i in range(0, l):
    m.append(0)
    m[i]=[]
    for j in range(0, c):
        m[i].append(float(input('Digite um elemento: ')))

print('\nMATRIZ')
for i in range(0, l):
    print()
    for j in range(0, c):
        print(m[i][j], end='        ')
        v.append(m[i][j])
        
print('\n\n', v)
