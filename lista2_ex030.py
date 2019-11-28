''' Seu algoritmo deve ler as variáveis inteiras A e B. Posteriormente, calcule o
Máximo Divisor Comum (MDC) entre A e B, a quantidade de divisores comuns entre A
e B e o Mínimo Múltiplo Comum (MMC) entre A e B.'''

def MDC(a, b):
    #UTILIZANDO A REGRA DAS DIVISÕES SUCESSIVAS
    while a%b!=0:
        aux=b
        b=a%b
        a=aux
    return(b)

def MMC(a, b):
    
    return()


A=int(input('Digite um número: '))
B=int(input('Digite outro número: '))
mdc=MDC(A, B)
MMC(A, B)


print('Números: {:1d} & {:1d}'.format(A, B))
print('MDC: {:1d}'.format(mdc))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                    #WIP
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#