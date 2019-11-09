'''Fazer um programa para acrescentar um elemento em uma lista se for digitado a letra “A”, remover se “R”, imprimir se “I” e 
sair se “F”.'''

lista=[]

op=input('\nDigite "A"(adicionar), "R"(remover), "I"(imprimir) ou "F"(finalizar): ').upper()

while op!='F':
    if op=='A':
        dado=input('\nDigite um dado para a lista: ')
        lista.append(dado)
    elif op=='R':
        pos=int(input('\nDigite a posição em que quer remover o elemento: '))
        lista.pop(pos)
    elif op=='I':
        print('\n', lista)
    else:
        print('\nOpção inválida.')
    op=input('\nDigite "A"(adicionar), "R"(remover), "I"(imprimir) ou "F"(finalizar): ').upper()
        
