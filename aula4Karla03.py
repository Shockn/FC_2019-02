lista=[]        #LISTA QUE RECEBE AS NOTAS
for i in range(0, 10):  #DEFININDO O NÚMERO DE NOTAS DA LISTA
    while True:         #LOOP PARA O TRATAMENTO DE ERRO (QUANDO UM INPUT FOR INSERIDO ERRADO, O FOR NÃO VAI PARA O PRÓXIMO i, E SIM CONTINUA NO MESMO ATÉ SER COLOCADO UM INPUT VÁLIDO).
        try:            
            nota=float(input('\nDigite a {:1d}° nota: '.format(i+1)))   #INPUT DAS NOTAS
            if nota in lista[0:i]:      #VERIFICA SE A NOTA JÁ APARECEU NA LISTA
                print('Nota repetida.')
            else:   #CASO SEJA UMA NOTA NOVA:
                if nota>10 or nota<0:   #CASO SEJA UMA NOTA INVÁLIDA
                    raise
                else:   #CASO SEJA UMA NOTA VÁLIDA
                    lista.append(nota)  #ADICIONA NA LISTA
                    #print(lista[0:i]) DEBUG
                    break   #QUEBRA O LOOP E VAI PARA O PRÓXIMO i DO FOR
        except:
            print('Nota inválida.')

#IMPRESSÃO DOS DADOS
print('\n',' NOTAS: '.center(20, '=')) 
for j in range(len(lista)):
    print('{:1d}° nota: {:1.1f}'.format((j+1), lista[j]).center(20))
