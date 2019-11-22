'''Crie um algoritmo que imprima os 4 primeiros números perfeitos.'''

perfeitos=[]

for i in range(1, 10000):
    total=0
    for j in range(1, i):
        if i%j==0:
            total+=j
    if total==i:
        perfeitos.append(total)

print('Os quatro primeiros números perfeitos:')
for i in range(0, len(perfeitos)):
    print(perfeitos[i], end=' ')

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
                #CUIDADO AO RODAR (MEIO PESADO)
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#                  