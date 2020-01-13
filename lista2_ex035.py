'''Jogo da subtração. Seu algoritmo deverá ler uma variável positiva T e 
posteriormente mais três variáveis positivas S1, S2 e S3, sendo que estas variáveis
são obrigatoriamente menores que T. O jogo consiste de dois jogadores, J1 e J2. A cada 
rodada a variável T é subtraída por uma das variáveis S1 ou S2 ou S3, escolhida pelo 
jogador da rodada. Perde o jogo quando o jogador ao executar sua subtração, obtém 
um valor menor do que zero. O seu programa deve apontar o jogador VENCEDOR.'''

import random

T=random.randint(1, 2000)

while T>=0:
    L=[]
    for i in range(0, 3):
        S=random.randint(1, T-1)
        L.append(S)
    for j in range(0, 3):
        print('S{:1d} = {:1d}'.format(j+1, L[j]))
    J1=input('\nJogador 1, escolha uma opção: ')