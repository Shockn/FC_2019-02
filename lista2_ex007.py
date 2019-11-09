'''Um anagrama (do grego ana = "voltar" ou "repetir" + graphein = "escrever")
é uma espécie  de  jogo  de  palavras,  resultando  do  rearranjo  das
letras  de  uma  palavra  ou frase  para  produzir  outras  palavras,
utilizando  todas  as  letras  originais  exatamente uma  vez.  Um  exemplo
conhecido  é  o  nome  da  personagem  Iracema,  claro  anagrama de América,
no  romance  de  José  de  Alencar. Implemente  a  função  anagrama(frase1,
frase2).  Os parâmetros frase1  e  frase2 são string.  A  função  deverá
retornar  True  se forem anagramas e False caso contrário.
Despreze acentuação(por exemplo: ã = a e ç = c) e os espaços não devem ser
computados para efeitos do anagrama.'''

def anagrama(frase1, frase2):
    f1=[]
    f2=[]
    if len(frase1)!=len(frase2):
        return(False)
    else:
        for i in range(0, len(frase1)):
            if i!=' ':
                f1.append(frase1[i])
                f2.append(frase2[i])
    f1.sort()
    f2.sort()

    if f1==f2:
        return(True)
    else:
        return(False)

f1=input('Digite uma palavra: ')
f2=input('Digite outra palavra: ')

if anagrama(f1, f2):
    print(('\n{:1s} e {:1s} são anagramas.').format(f1, f2))
else:
    print(('\n{:1s} e {:1s} não são anagramas.').format(f1, f2))
