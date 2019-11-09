soma=0
lista=[]

for i in range(0, 5):
    num=float(input('Digite um número [{:1d}]: '.format(i)))
    lista.append(num)

for j in range(len(lista)):
    if lista[j]%2==0:
        soma+=lista[j]
    if j%2!=0:
        soma-=lista[j]

print('\nO total da soma é: {:1.2f}'.format(soma))
