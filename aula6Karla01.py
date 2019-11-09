'''Fazer um módulo para receber dois valores inteiros e retornar a soma dos multiplosde 7 MENOS a soma dos multiplos 
de 13 ENTRE esses valores.'''

def somaMult(x, y):
    soma=0
    for i in range(x+1, y):
        if i%7==0:
            soma+=i
        elif i%13==0:
            soma-=1
    return(soma)

j=int(input('Digite o primeiro número: '))
k=int(input('Digite o segundo número: '))

print('Resultado: ',somaMult(j,k))
