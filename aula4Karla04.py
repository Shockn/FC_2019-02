lista=[]    #LISTA QUE VAI CONTER AS NOTAS
cont=2      #CONTADOR PARA PRINTAR A POSIÇÃO DAS NOTAS A PARTIR DA 1°

while True:     #LOOP PARA O TRATAMENTO DE ERRO DA 1° NOTA
    try:
        nota=float(input('\nDigite a 1° nota: '))
        if nota<0 or nota>10:   
            raise
        break
    except:
        print('Nota inválida.')

while nota>=0:      #ENQUANTO AS NOTAS A PARTIR DA 1° FOREM MAIORES QUE ZERO
    lista.append(nota)  
    while True: #TRATAMENTO DE ERRO DAS N NOTAS
        try:
            nota=float(input('\nDigite a {:1d}° nota: '.format(cont)))
            if nota>10:
                raise
            elif nota in lista:     #VERIFICANDO SE A NOTA JÁ FOI REPETIDA
                print('Nota repetida.')
            else:
                break
        except:
            print('Valor inválido.')
    cont+=1     #APÓS A ENTRADA DE UMA NOTA VÁLIDA, O CONTADOR AUMENTA

#IMPRESSÃO DAS NOTAS
print('\n','NOTAS'.center(20, '='))
for i in range(len(lista)):
    print('{:1d}° nota: {:1.1f}'.format((i+1),lista[i]).center(20))
    
