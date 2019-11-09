'''Fazer um módulo para receber um vetor como parâmetro e
retornar um outro vetor sem repetições'''


def VetCheck(vet):
    vet2=[]
    backup=vet
    for i in range(0, len(vet)):
        result=False
        for j in range(i+1, len(vet)):
            if vet[i]==vet[j]:
                result=True
        if result==False:
            vet2.append(vet[i])
    #vet2.sort()
    return(vet2)

vetor=[]
num=input('Digite um número para o vetor: ')
while num.isdigit()==True:
    vetor.append(num)
    num=input('Digite um número para o vetor: ')

print('\nVetor sem repetições: ', VetCheck(vetor))

