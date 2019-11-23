'''Crie um algoritmo se imprima os N primeiros números que sejam primos e façam parte da série de Fibonacci
UTILIZANDO OBRIGATORIAMENTE FUNÇÕES.'''

#ESCREVE A SEQUÊNCIA DE FIBONACCI ENQUANTO O F1 FOR MENOS QUE O N
def fibonacci(n):
    sequencia=[]
    f1=0
    f2=1
    f=0
    while f1<n:
        sequencia.append(f1)
        aux=f2
        f=f1+f2
        f2=f
        f1=aux   
    return(sequencia)

#ENCONTRA OS NÚMEROS PRIMOS NA SEQUÊNCIA
def primos(sequencia):
    nPrimos=[]
    for i in sequencia:
        primo=True
        for j in range(2, i):
            if i%j==0:
                primo=False
        if primo==True:
            nPrimos.append(i)
    nPrimos.pop(0)
    nPrimos.pop(1)
    return(nPrimos)
    
#CHAMA AS FUNÇÕES
num=int(input('Digite um número: '))
sequencia=fibonacci(num)
nPrimos=primos(sequencia)

#IMPRIME OS DADOS
print('\nSequência de Fibonacci até {:1d}:'.format(num))
for i in range(0, len(sequencia)):
    print(sequencia[i], end=' ')

print('\n\nNúmeros primos até {:1d} na sequência de Fibonacci: '.format(num))
for i in range(len(nPrimos)):
    print(nPrimos[i], end=' ')