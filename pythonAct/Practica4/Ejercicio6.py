from pattern.es import conjugate,INFINITIVE,verbs,parse,split
import json
import os

def leer_texto():
    f=open('frase.txt','r',encoding='UTF-8')
    frase=str(f.read())
    f.close()
    return frase

def generar_archivo_verbos(frase):
    s=parse(frase).split()
    lis_verbos=[]
    for cada in s:
        for c in cada:
            if c[1]=='VB':
                lis_verbos=lis_verbos+[conjugate(c[0],INFINITIVE)]
    set_verbos=set(lis_verbos)
    print(lis_verbos)
    print(set_verbos)
    jason={}
    for verbo in set_verbos:
        jason[verbo]={'cant_apariciones':lis_verbos.count(verbo)}
    print(jason)
    j=open('verbos.json','w')
    json.dump(jason,j,indent=4)

os.chdir('Archivos6')
frase=leer_texto()
print(frase)
generar_archivo_verbos(frase)



