import time
import PySimpleGUI as sg
import json
import os


os.chdir('Archivos4')
hora_act=time.asctime()
layout=[
            [sg.Text('Ingrese la temperatura:')],
            [sg.InputText(key='temp')],
            [sg.Text('Ingrese la humedad:')],
            [sg.InputText(key='hume')],
            [sg.Button('Sumbit'),sg.Button('Close')]
        ]

window=sg.Window('Temperatura y Humedad',layout)
lis=[]
while True:
    event,values=window.read()
    if event in ('Close',None):
        break
    elif event=='Sumbit':
        temp_dev='temperatura: '+str(values['temp'])
        hum_dev='humedad: '+str(values['hume'])
        datos=temp_dev+' '+hum_dev+' '+str(hora_act)
        jason=[
            {"temperatura":str(values['temp']),
            "humedad":str(values['hume']),
            "hora":str(hora_act)}
        ]
        lis=lis+[datos]

        print(lis)
        window.close()

        layout2=[
                [sg.Text('Do you want to add this data to the file?')],
                [sg.Button('Yes'),sg.Button('No')]
        ]

        window2=sg.Window('Question',layout2)

        event2,values2=window2.read()

        if event2=='Yes':
            f=open('archivoEj4.txt','a',encoding='UTF-8')
            json.dump(jason,f)
            f.close()


        sg.popup('Ingresaste',lis)
