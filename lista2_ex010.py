'''Crie a função mat_transposta(matriz). A função deve receber uma matriz
genérica bidimensional,  de  qualquer  tamanho  (não  necessariamente
quadrada)  e  retornar  a matriz transposta, sem alterar a matriz original.'''

import random

#GERADOR DA TRANSPOSTA

def mat_transposta(matriz):
    m2=[]
    m2=[None]*c
    for i in range(0, c):
        m2[i]=[None]*l
        for j in range(0, l):
            m2[i][j]=matriz[j][i]       
    return(m2)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

#GERADOR DA MATRIZ ORIGINAL

m=[]
l=random.randint(2, 4)
c=random.randint(2, 4)

for i in range(0, l):
    m.append(None)
    m[i]=[]
    for j in range(0, c):
        m[i].append(random.randint(0, 9))

#IMPRESSÃO DAS MATRIZES

print('MATRIZ ORIGINAL:')
for i in range(0, l):
    print()
    for j in range(0, c):
        print(m[i][j], end=' ')

print('\n\nMATRIZ TRANSPOSTA:')           
for i in range(0, c):
    print()
    for j in range(0, l):
        print(mat_transposta(m)[i][j], end=' ')
