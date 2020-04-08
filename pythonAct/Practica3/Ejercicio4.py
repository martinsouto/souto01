anim={'Gato Montes':2,'Yacare overo':4,'Boa acuática':5}
claves=anim.keys()

for nombre in claves:
    pal=[]
    for i in range(len(nombre)):
        if (i!=anim[nombre]):
            pal+='_'
        else:
            pal+=[nombre[i]]
    print(pal)