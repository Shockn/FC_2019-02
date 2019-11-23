'''Crie um algoritmo que leia N números inteiros positivos e responda se é possível formar um polígono com o
mesmo (dica: maior número < soma dos demais números).'''

lado=float(input('Digite o tamanho do lado: '))
lados=[]
while lado>0:
    lados.append(lado)
    lado=float(input('Digite o tamanho do lado: '))

for i in range(0, len(lados)):
    somaLados=0
    pol=True
    for j in range(len(lados)):
        if i!=j:
            somaLados+=lados[j]
    if somaLados<lados[i]:
        pol=False
        break

if pol==False:
    print('\nNão é possível formar um polígono.')
else:
    print('\nÉ possível formar um polígono.')