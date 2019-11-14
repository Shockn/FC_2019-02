'''Fazer um programa para ler 5 nomes e 5 notas e guardar em um arquivo.'''

f=open('aula10Karla01.txt', 'w')
for i in range(0, 5):
    nome=input('Digite um nome: ')
    nota=float(input('Digite uma nota: '))
    f.write(nome+' '+str(nota)+'\n')
f.close()