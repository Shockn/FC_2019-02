'''Crie uma matriz 5x5 com 1 na diagonal principal e 0 nas outras posições.
Imprima a matriz no formato tradicional de linhas e colunas.'''

m=[]
m=[None]*5

for i in range(0, 5):
    m[i]=[None]*5
    for j in range(0, 5):
        if m[i]==m[j]:
            m[i][j]=1
        else:
            m[i][j]=0

print('\n',str('MATRIZ').rjust(8))
for i in range(0, 5):
    print()
    for j in range(0, 5):
        print(m[i][j], end='  ')
