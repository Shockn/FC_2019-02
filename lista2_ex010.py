'''Crie a função mat_transposta(matriz). A função deve receber uma matriz
genérica bidimensional,  de  qualquer  tamanho  (não  necessariamente
quadrada)  e  retornar  a matriz transposta, sem alterar a matriz original.'''

import random

def mat_transposta(matriz):
    m2=[]
    for i in range(0, l):
        m2.append(None)
        m2[i]=[]
        for j in range(0, c):
            m2[i].append(matriz[i][j])
            return(m2[i][j])

m=[]
l=random.randint(1, 5)
c=random.randint(1, 5)

for i in range(0, l):
    m.append(None)
    m[i]=[]
    for j in range(0, c):
        m[i].append(random.randint(0, 9))

for i in range(0, c):
    print()
    for j in range(0, l):
        a=mat_transposta(m)
        print(a, end=' ')
