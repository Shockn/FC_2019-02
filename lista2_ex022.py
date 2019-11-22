''' Crie um algoritmo que leia um número N e calcule:
somatório de i=1 até n de 1/i'''

n=int(input('Digite um número: '))
soma=0

for i in range(1, n+1):
    soma+=1/i
    print('Somatório: {:1.2f}'.format(soma))

          