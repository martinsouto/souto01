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


colores = ['azul','amarillo','rojo','blanco','negro']
coordenadas = [(2,3),(5,6),(8,8),(10,2),(-5,-8)]
dic1=crear_dic_sr(colores,coordenadas)
dic2=crear_dic_cr(coordenadas,colores)
