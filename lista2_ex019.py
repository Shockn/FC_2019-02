'''Crie um algoritmo que leia um número N e imprima os N primeiros números primos. O seu programa 
deve fazer o MÍNIMO de interações possíveis.'''

n=int(input('Digite um número: '))

for i in range(3, n+1):
    primo=True
    for j in range(i+1, n):
        if i%j==0:
            primo=False
        else:
            primo=True

if primo==True:
    print('É primo.')
else:
    print('Não é primo.')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
            'W.I.P.'
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#