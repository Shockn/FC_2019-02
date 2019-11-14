'''Fazer um programa para ler o arquivo criado e imprimir o nome do
aluno que tirou a maior nota e a média da turma.'''

f=open('teste.txt', 'w')

nome=input('Digite o nome do aluno: ')
while nome!='':
    nota=float(input('Digite a nota do aluno: '))
    f.write(nome+' '+str(nota)+'\n')
    nome=input('Digite o nome do aluno: ')

f.close()

f=open('teste.txt', 'r')

maiorNota=0
maiorNome=''
cont=media=0

for i in f:
    nome, nota=i.split(' ')
    nota=float(nota)
    if nota>maiorNota:
        maiorNota=nota
        maioNome=nome
    media+=nota
    cont+=1

media=media/cont

print('\nO aluno {:1s} teve a maior nota: {:1.2f}.'.format(nome, nota))
print('A média da turma foi: {:1.2f}.'.format(media))
    
    
