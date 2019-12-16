'''Jogo de dados. Dois jogadores estão confrontando-se entre si, usando dois dados,
numerados de 1 até 6 (dado random.randint(1,6)). Vence uma rodada quem obtiver
o maior número no lançamento. Entretanto, caso um jogador obtiver um lançamento
com dois dados iguais (por exemplo, 1 e 1, 2 e 2,....) e o outro jogador não, 
o jogador que tiver lançado a dupla ganha. Caso os dois jogadores fizerem o
lançamento e o resultado for de duas duplas para os dois jogadores, ganha o jogador 
com a dupla maior. A disputa é em 11 lançamentos. Indique o jogador vencedor ou se
houve empate.'''

import random

w1=w2=0
for i in range(1, 12):
    p1=[]
    p2=[]
    for j in range(0, 2):
        p1.append(random.randint(1, 6))
        p2.append(random.randint(1, 6))
    
    soma1=p1[0]+p1[1]
    soma2=p2[0]+p2[1]
    if p1[0]==p1[1] and p2[0]!=p2[1]:
        w1+=1
    elif p2[0]==p2[1] and p1[0]!=p1[1]:
        w2+=1
    else:
        if soma1>soma2:
            w1+=1
        elif soma2>soma1:
            w2+=1
        else:
            pass    

    #####DEBUG#####
    print("Player 1:", p1)
    print("Player 2:", p2)
    print("({:1d}) P1 Wins: {:1d} - P2 Wins: {:1d}".format(i, w1, w2))
    print()
    ##############

if w1>w2:
    print('\nO player 1 venceu com {:1d} vitórias!'.format(w1))
elif w2>w1:
    print('\nO player 2 venceu com {:1d} vitórias!'.format(w2))
else:
    print('\nA disputa terminou em empate.')

    