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
print(dic.keys())
print(max(dic, key=lambda usuario: dic[usuario][1]))
nom_us=input('nombre de usuario')
datos_us=[1,10,1]
if (nom_us in dic):
    if (datos_us[1]>dic[nom_us][1]):
        dic[nom_us]=datos_us
else:
    dic[nom_us]=datos_us
dic_ord=sorted(dic, key=lambda usuario: dic[usuario][1], reverse=True)
cont=0
for i in dic_ord:
    if (cont<10):
        cont+=1
        print(dic_ord[i])

