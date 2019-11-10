'''Crie  a  função mat_maior_10(matriz).  A  função  deve  receber  uma
matriz  genérica, de  qualquer  tamanho  (não  necessariamente  quadrada)
e  retornar  a  quantidade  de elementos da matriz maiores que dez.'''

import random

#RETORNA OS ELEMENTOS MAIORES QUE DEZ

def mat_maior_10(matriz):
    a=[]
    for i in range(0, l):
        for j in range(0, c):
            if matriz[i][j]>10:
                a.append(matriz[i][j])
    return(a)

#MATRIZ

m=[]
l=random.randint(2, 4)
c=random.randint(2, 4)

for i in range(0, l):
    m.append(0)
    m[i]=[]
    for j in range(0, c):
        m[i].append(random.randint(0, 50))

#IMPRESSÃO DA MATRIZ

print('MATRIZ:')
for i in range(0, l):
    print()
    for j in range(0, c):
        print(str(m[i][j]).center(5), end='  ')

#IMPRESSÃO DOS VALORES MAIORES QUE DEZ

print('\n\nVALORES MAIORES QUE DEZ:\n')
for i in range(0, len(mat_maior_10(m))):
    print(mat_maior_10(m)[i], end=' ')
                    
