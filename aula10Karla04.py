'''Fazer um programa para ler o arquivo criado e criar um outro arquivo
contendo apenas os nomes dos alunos que tiveram nota acima da média da
turma.'''

#ABRE O 1 ARQUIVO

f=open('aula10Karla04.txt', 'w')

#ESCRE OS DADOS
nome=input('Digite um nome: ')
while nome!='':
    nota=float(input('Digite uma nota: '))
    f.write(nome+' '+str(nota)+'\n')
    nome=input('Digite um nome: ')

f.close() #FECHA O 1 ARQUIVO


#ABRE O 1 ARQUIVO NOVAMENTA PARA A LEITURA
f=open('aula10Karla04.txt', 'r')

media=cont=0

for i in f:
    nome, nota=i.split()
    nota=float(nota)
    media+=nota
    cont+=1
media=media/cont

f.close()  #FECHA O 1 ARQUIVO NOVAMENTE

#ABRE O 1 ARQUIVO PARA LEITURA NOVAMENTE E O 2 PARA ESCRITA
f=open('aula10Karla04.txt', 'r')
f2=open('aula10Karla04_2.txt', 'w')

#PEGA OS ACIMA DA MÉDIA DO 1 E ESCREVE NO 2
for j in f:
    nome, nota=j.split()
    nota=float(nota)
    if nota>=media:
        f2.write(nome+' '+str(nota)+'\n')

#FECHA AMBOS
f2.close()
f.close()


