def ingreso_usuarios():   
    ok='si'
    d={}
    while (ok=='si'):
        nom=input('ingrese nombre de usuario')
        if nom not in d:
            d[nom]=[int(input('ingrese nivel alcanzado')),int(input('ingrese puntaje máximo')),float(input('ingrese tiempo de juego'))]
        else:
            print('este nombre de usuario ya esta registrado, intente con otro')
        ok=input('usuario ingresado correctamente, desea ingresar otro?(si o no)')
    print(d)
    return d



dic=ingreso_usuarios()
print(dic['martin'])
print(list(dic.keys()))
print(max(dic, key=lambda usuario: dic[usuario][1]))
nom_us=input('nombre de usuario')
datos_us=[1,10,1]
if (nom_us in dic):
    if (datos_us[1]>dic[nom_us][1]):
        dic[nom_us]=datos_us
else:
    dic[nom_us]=datos_us

lis_usuarios_ord=sorted(dic, key=lambda usuario: dic[usuario][1], reverse=True)
print(lis_usuarios_ord)
print('Mejores 10: ')
print(lis_usuarios_ord[:10])

#asi si se puede indexar keys y todo eso 
print(list(dic.keys())[1])

#----------------------------EJERCICIO7----------------------------------------
def diez_primeros(d):
    lis_usuarios_ord=sorted(d, key=lambda usuario: d[usuario][1], reverse=True)
    print(lis_usuarios_ord)
    cont=0
    for i in lis_usuarios_ord:
        if (cont<10):
            print('puntuacion: '+str(d[lis_usuarios_ord[cont]][1]))
            cont+=1

def dic_ord_apellido(d):
    print(sorted(d))
    print(list(map(lambda x: d[x]   ,sorted(d))))

diez_primeros(dic)
dic_ord_apellido(dic)