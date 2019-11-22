'''Crie um algoritmo que leia um número N e verifique se ele é primo. O seu
programa deve fazer o MÍNIMO de interações possíveis.'''

n=int(input('Digite um número: '))

primo=True
for i in range(2, n):
    if n%i==0:
        primo=False

if primo:
    print('É primo.')
else:
    print('Não é primo.')