'''Jogo da subtração. Seu algoritmo deverá ler uma variável positiva T e 
posteriormente mais três variáveis positivas S1, S2 e S3, sendo que estas variáveis
são obrigatoriamente menores que T. O jogo consiste de dois jogadores, J1 e J2. A cada 
rodada a variável T é subtraída por uma das variáveis S1 ou S2 ou S3, escolhida pelo 
jogador da rodada. Perde o jogo quando o jogador ao executar sua subtração, obtém 
um valor menor do que zero. O seu programa deve apontar o jogador VENCEDOR.'''

import random

def Sgen(T):
    print('\n*NOVO TURNO*')
    L=[]
    for i in range(0, 3):
        L.append(random.randint(1, T-1))
    #print(L)
    return(L)

def Choices(L):
    print()
    for i in range(0, len(L)):
        print('S{:1d} ='.format(i+1), L[i]) 
    return()

def J1(T, L):
    while True:
        try:
            play=input('\nJogador 1, faça sua escolha: ').upper()
            if play=="S1" and L[0]!="---":
                T-=L[0]
                L[0]="---"
                print("\nT =", T)
            elif play=="S2" and L[1]!="---":
                T-=L[1]
                L[1]="---"
                print("\nT =", T)
            elif play=="S3" and L[2]!="---":
                T-=L[2]
                L[2]="---"
                print("\nT =", T)
            else:
                raise
            break
        except:
            print('Escolha inválida.')
    return(T)

def J2(T, L):
    while True:
        try:
            play=input('\nJogador 2, faça sua escolha: ').upper()
            if play=="S1" and L[0]!="---":
                T-=L[0]
                L[0]="---"
                print("\nT =", T)
            elif play=="S2" and L[1]!="---":
                T-=L[1]
                L[1]="---"
                print("\nT =", T)
            elif play=="S3" and L[2]!="---":
                T-=L[2]
                L[2]="---"
                print("\nT =", T)
            else:
                raise
            break
        except:
            print('Escolha inválida.')
    return(T)


#PROGRAMA PRINCIPAL

T=random.randint(1, 2000)
print("\nT =", T)

while T>=0:
    
    L=Sgen(T)
    Choices(L)
    print("\nT =", T)
    
    for i in range(0, 2):
        if i==0:
            T=J1(T, L)
            Choices(L)
        else:
            T=J2(T, L)
            Choices(L)

print('\nFim de Jogo!')