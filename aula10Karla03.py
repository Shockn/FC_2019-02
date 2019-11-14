'''Fazer um programa para ler o arquivo criado e imprimir o nome do aluno que tirou a maior 
nota e a média da turma'''

f=open('aula10Karla03.txt', 'w')

nome=input('Digite o nome do aluno: ')
nota=float(input('Digite a nota do aluno: '))
while nome!='':
    f.write(nome+' '+str(nota)+'\n')
    nome=input('Digite o nome do aluno: ')
    nota=float(input('Digite a nota do aluno: '))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                        'EM PROGRESSO'
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
