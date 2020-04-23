import random

def crear_dic_cr(claves,valores):
    dic={}
    for i in claves:
        dic[i]=random.choice(valores)
    print(dic)
    return(dic)

def crear_dic_sr(claves,valores):
    vals=valores[:]
    dic={}
    for i in claves:
        palabra=random.choice(vals)
        dic[i]=palabra
        vals.remove(palabra)
    print(dic)
    return(dic)

def azul ():
    x=random.randint(1,100)
    y=random.randint(1,100)
    g=int(input('cual es el resultado de la suma entre '+str(x)+' y '+str(y)+' ?'))
    if (g==(x+y)):
        print('acertaste!')
    else:
        print('fallaste')

def amarillo():
    palabras = [('grave',['molesto']), ('aguda',['ratón']),('esdrujula',['murciélago'])]
    tup_al=random.choice(palabras)
    pal_al=random.choice(tup_al[1])
    print(pal_al)
    resp=input('de que tipo es esta palabra?')
    if resp.lower()==tup_al[0]:
        print('acertaste')
    else:
        print('fallaste')


colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dic1=crear_dic_sr(colores,coordenadas)
dic2=crear_dic_cr(coordenadas,colores)
eleccion=dic2[random.choice(coordenadas)]
if ((eleccion=='azul')or(eleccion=='rojo')or(eleccion=='negro')):
    azul()
elif ((eleccion=='amarillo')or(eleccion=='blanco')):
    amarillo()