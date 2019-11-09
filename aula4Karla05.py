'''Fazer um programa para ler dados positivos para dois vetores e imprimir a interseção desses vetores'''

vet1=[]
vet2=[]
inter=[]

num=int(input('\nDigite um número para o vetor 1: '))
while num>0:
    vet1.append(num)
    num=int(input('\nDigite um número para o vetor 1: '))
print(vet1)

num=int(input('\nDigite um número para o vetor 2: '))
while num>0:
    vet2.append(num)
    num=int(input('\nDigite um número para o vetor 2: '))
print(vet2)

for i in range(0, len(vet1)):
    for j in range(0, len(vet2)):
        if vet1[i]==vet2[j]:
            inter.append(vet1[i])

print('\nInterseções:', inter)
