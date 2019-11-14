'''Fazer um programa para ler um arquivo e imprimir o conteúdo deste arquivo na tela.'''

f=open('aula10Karla02.txt', 'r')
impressao=f.read()
print(impressao)
f.close()