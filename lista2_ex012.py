'''Cálculo aproximado de ∏ (Pi) pelo Método de Monte Carlo.
Dada a função: x^2+ y^2<=4,
calcule o valor aproximado de ∏ com 4.10^6 interações.
Dicas: use random.random() * 2  para  gerar  valores  entre  0  e  2 para
as  variáveis  x  e  y e conte  o  número  de  pontos (x,y) que satisfazem a
equação dada e dividao resultado por 10^6. Cuidadocom o tipo de dados.'''

import random

def funcao(x, y):
    if x**2+y**2<=4:
        pi=0
        pi=4-x
        y=pi
        pi=x+y
    else:
        pass
    return(pi)

x=float(random.random()*2)
y=float(random.random()*2)

print(funcao(x, y))



#NÃO ENTENDI A PROPOSTA DO EXERCÍCIO
