def crear_dic (frase):
    conj=set(frase.split(' '))
    print(conj)
    dic={}
    for i in conj:
        if len(i) in dic:
            dic[len(i)]+=[i]
        else:
            dic[len(i)]=[i]
    return dic

frase='''Si trabajás mucho CON computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número DE archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o UN juego simple.'''
dic=crear_dic(frase)
print(dic)