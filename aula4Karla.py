'''Fazer um programa para ler as notas de uma turma de 40 alunos, 
imprimir a qtd dos alunos ACIMA da média da turma.'''

notas=[]
soma=0
cont=0

for i in range(40):
    nota=float(input('Digite uma nota: '))
    notas.append(nota)
    soma+=nota

media=soma/len(notas)
   
for j in range(len(notas)):
    if notas[j]>media:
        cont+=1

print('\nMédia: {:1.2f}\nQuantidade de alunos acima da média: {:1d}'.format(media, cont))
    
    
