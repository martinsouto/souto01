import csv
import PySimpleGUI as sg
import os

def cantidad_mujeres(csvreader):
    dic_cantmujeres={}
    for fila in csvreader:
        if fila['Estudiantes Mujeres']!='':
            if fila['Institución'] in dic_cantmujeres:
                dic_cantmujeres[fila['Institución']]+=int(fila['Estudiantes Mujeres'])
            else:
                dic_cantmujeres[fila['Institución']]=int(fila['Estudiantes Mujeres'])
    for elem in dic_cantmujeres:
        print(elem+': '+str(dic_cantmujeres[elem]))
    return dic_cantmujeres

def imprimir_ordenado(dic):
    print('-'*50)
    lis_items=list(dic.items())
    lis_ord=sorted(lis_items,key=lambda facu: facu[1])
    for i in lis_ord:
        print(i[0]+': '+str(i[1]))
    return lis_ord

def mostrar_py(lis_items):
    layout=[
        [sg.Text('Cantidad de mujeres por universidad')],
        [sg.Listbox(lis_items,size=(40,10))],
        [sg.Button('Ok')]
    ]
    window=sg.Window('Info universidades',layout)
    window.read()
    window.close()   


os.chdir('Archivos_10')
archi=open('mujeresEncarrera.csv','r',encoding='UTF-8',newline='')
csvreader=csv.DictReader(archi)
dic_cantmujeres=cantidad_mujeres(csvreader)
lis_items=imprimir_ordenado(dic_cantmujeres)
mostrar_py(lis_items)