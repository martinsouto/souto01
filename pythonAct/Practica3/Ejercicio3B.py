def ingreso_usuarios():
    ok='si'
    d={}
    while(ok=='si'):
        nom_usuario=input('Ingrese el nombre de usuario')
        if (nom_usuario not in d):
            nivel=int(input('Ingrese nivel alcanzado'))
            puntaje=int(input('Ingrese puntaje alcanzado'))
            tiempo=float(input('Ingreese tiempo de juego'))
            d[nom_usuario]={'nivel':nivel,'puntaje':puntaje,'tiempo':tiempo}
            ok=input('usuario ingresado correctamente, desea ingresar otro?(si o no)')
        else:
            print('este nombre de usuario ya esta registrado, intente con otro')
    return d


dic=ingreso_usuarios()
print(dic)
lis_items=dic.items()
lis_keys=dic.keys()
print('Usuarios que jugaron: '+str(lis_keys))
print('Usuario con mayor puntaje: '+str((max(lis_items, key=lambda usuario: usuario[1]['puntaje']))))
nom_nuevo='tomas'
datos_nuevo={'nivel':3,'puntaje':60,'tiempo':float(4)}
if (nom_nuevo in dic):
    if (dic[nom_nuevo]['puntaje']>datos_nuevo['puntaje']):
        dic[nom_nuevo]=datos_nuevo
else:
    dic[nom_nuevo]=datos_nuevo
lis_ord=sorted(lis_items, key=lambda usuario: usuario[1]['puntaje'],reverse=True)[:10]
print('mejores 10 ')
print(lis_ord)