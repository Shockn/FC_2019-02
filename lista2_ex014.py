'''Faça um programa que calcule o valor de PI pela soma dos n primeiros
termos da série abaixo:
raíz ( 12 * (1 - 1/4 +1/9 - 1/16 + 1/25 - 1/16 ... )'''

import math

def pi(n):
    pi=0
    for i in range(1, n+1):
        if i%2==0:
            pi-=1/(i**2)
        else:
            pi+=1/(i**2)
    pi=pi*12
    pi=math.sqrt(pi)
    return(pi)

n=int(input('Digite um n: '))
print('Pi: ', pi(n))
