'''Implemente seguinte algoritmo de criptografia: dada uma frase qualquer, se o
código ASCII do caractere for par, subtraia três do código ASCII. Se for ímpar, 
some três (semelhante ao exemplo dado em sala).'''

def cripto(frase):
    fCripto=""
    for i in range(0, len(frase)):
        a=None
        if ord(frase[i])%2==0:
            a=ord(frase[i])-3
            fCripto+=chr(a)
        else:
            a=ord(frase[i])+3
            fCripto+=chr(a)
    return(fCripto)

f=input("Digite uma frase: ")
print('\nFrase original: {:1s}\nFrase criptogragada: {:1s}'.format(f, cripto(f)))

            
