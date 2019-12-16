'''Leia um número A real positivo. Calcule sua raiz real utilizando o método babilônico 
indo até a 10° interação (x10). Considere, por hipótese, x0 = 1.
xn+1=(xn+a/xn)/2'''

a=float(input('Digite um número real: '))
xn=0
print()

while xn<=10:
    if xn==0:
        x=1
        print(xn, x)
        xn+=1
    else:
        x=(xn+(a/xn)/2)
        print(xn, x)
        xn+=1
    
#NÃO ENTENDI MT BEM :(
    





 