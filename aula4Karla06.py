'''Fazer um programa para ler dados para um vetor. Criar um outro vetor a partir dos elementos do vetor 1, onde os elementos de 
índices (ordem) par são multiplicados por 2 e os de ordem ímpar multiplicados por 3 e diminuídos de 1. No final imprimir os dois 
vetores'''

vet1=[]
vet2=[]

num=int(input('\nDigite um número para o vetor: '))
while num>0:
    vet1.append(num)
    num=int(input('Digite um número para o vetor: '))

for i in range(len(vet1)):
    if i%2==0:
        vet2.append(vet1[i]*2)
    else:
        vet2.append(vet1[i]*3-1)

print('\nPrimeiro vetor:', vet1)
print('Segundo vetor:', vet2)
