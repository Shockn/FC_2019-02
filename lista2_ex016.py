''' Crie um algoritmo que:
a) Leia e escreva o nome e a altura das moças inscritas em um concurso de
beleza, até que seja digitada o nome ‘MARIA’, que marca o final da lista, mas é
para ser computada no concurso.
b) Calcule e escreva as duas maiores alturas e quantas moças as possuem.'''

l=[]

#INSERE OS DADOS NA LISTA
altura=float(input('Digite a altura: '))
nome=input('Digite o nome: ').upper()
l.append(nome)
l.append(altura)
while nome!='MARIA':
    altura=float(input('Digite a altura: '))
    nome=input('Digite o nome: ').upper()
    l.append(nome)
    l.append(altura)

print('\n')

#ACHA AS ALTURAS
mAltura=mAltura2=0
mAltQTD=mAlt2QTD=0

for i in range(0, len(l)):
    if i%2==0:
        pass
    else:
        if l[i]>mAltura:
            mAltura=l[i]
        elif l[i]<mAltura:
            if l[i]>mAltura2:
                mAltura2=l[i]

for i in range(0, len(l)):
    if l[i]==mAltura:
        mAltQTD+=1
    elif l[i]==mAltura2:
        mAlt2QTD+=1

#IMPRIME OS DADOS
print('Maior Altura: {:1.2f} - Quantidade com essa altura: {:1d}.'.format(mAltura, mAltQTD))
print('2° Maior Altura: {:1.2f} - Quantidade com essa altura {:1d}.'.format(mAltura2, mAlt2QTD))
    
    
