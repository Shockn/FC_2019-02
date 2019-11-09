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
