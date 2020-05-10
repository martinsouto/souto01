import PySimpleGUI as sg

lista=['hola','chau','bokee',3]

layout=[
    [sg.Text('Probando')],
    [sg.Listbox(values=lista,size=(10,1),key='lis_')],
    [sg.Button('Ok'),sg.Button('Cancel')]
]
window=sg.Window('Prueba ListBox',layout)


event,values=window.read()
print(values)
if event=='Ok':
    if values['lis_'][0]=='hola':
        print('funciona')
window.close()
#-----------------------------------------------------------------------
lis_juegos=['Ahorcado','Ta Te Ti','Otello',]

layout=[
    [sg.Text('Elija el juego que quiere jugar')],
    [sg.Listbox(values=lis_juegos,size=(40,4),key='lis_')],
    [sg.Button('Jugar'),sg.Button('Salir')]
]
window=sg.Window('Juegos',layout)

while True:
    event,values=window.read()
    window.Hide()
    if event=='Jugar':
        if values['lis_'][0]=='Ahorcado':
            x=input('ahorcadoo')
        elif values['lis_'][0]=='Ta Te Ti':
            x=input('tatetii')
        elif values['lis_'][0]=='Otello':
            x=input('otellooo')
        window.UnHide()
    else:
        break

window.close()
