'''Uma certa firma fez uma pesquisa para saber se as pessoas gostaram ou não de um novo produto lançado no 
mercado. Para isso, forneceu o sexo do entrevistado e sua resposta (sim ou não). Sabendo-se que foram 
entrevistadas 2.000 pessoas, crie um algoritmo que calcule e escreva:
a) o número de pessoas que responderam sim;
b) o número de pessoas que responderam não;a porcentagem de pessoas do sexo masculino que responderam não.'''

import random

respostas=['SIM', 'NÃO']
genero=['M', 'F']
s=n=m=total=0

for i in range(0, 20):
    sexo=genero[random.randint(0, 1)]
    resposta=respostas[random.randint(0, 1)]
    total+=1
    if resposta=='SIM':
        s+=1
    elif resposta=='NÃO':
        if sexo=='M':
            m+=1
            n+=1
        else:
            n+=1
    print(sexo, resposta)

print(m)

mN=(m*100)/n

print('\n{:1d} pessoas responderam SIM'.format(s))
print('{:1d} pessoas responderam NÃO'.format(n))
print('{:1.2f}% foi a porcentagem de homens que responderam NÃO'.format(mN))


