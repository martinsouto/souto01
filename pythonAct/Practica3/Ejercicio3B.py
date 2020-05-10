import PySimpleGUI as sg
import json

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

def modificoDatos(users):
    
    layout=[
        [sg.Text('Ingrese datos de usuario nuevo o existente')],
        [sg.Text('Nombre:')],
        [sg.InputText(key='nom_',size=(40,1))],
        [sg.Text('Nivel alcanzado:')],
        [sg.InputText(key='nivel_',size=(40,1))],
        [sg.Text('Puntaje alcanzado:')],
        [sg.InputText(key='puntaje_',size=(40,1))],
        [sg.Text('Tiempo de juego:')],
        [sg.InputText(key='tiempo_',size=(40,1))],
        [sg.Button('Enter')],
    ]
    window=sg.Window('Enter user',layout)
    event,values=window.read()
    if event=='Enter':
        f=open('usuariosJSON.txt','r')
        data=json.load(f)
        f.close()
        data[values['nom_']]={'nivel':values['nivel_'],'puntaje':values['puntaje_'],'tiempo':values['tiempo_']}
        f=open('usuariosJSON.txt','w')
        json.dump(data,f,indent=4)
        f.close()
    window.close()


def importacion(usu):
    layout=[
        [sg.Text('Do you want to export users to a file?')],
        [sg.Button('Yes'),sg.Button('No')]
    ]
    window=sg.Window('Importation',layout)
    event,values=window.read()
    print(event)
    if event=='Yes':
        f=open('usuariosJSON.txt','w')
        json.dump(usu,f,indent=4)
        f.close()
        f=open('usuariosJSON.txt','r')
        data=json.load(f)
        print(data)
        f.close()
        modificoDatos(usu)
    window.close()


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

importacion(dic)