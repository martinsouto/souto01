import PySimpleGUI as sg
#prueba de pop ups get folder y get file y prueba de .disable()
layout=[
    [sg.Text('prueba de disable y eso')],
    [sg.Button('Probar'),sg.Button('Carpeta'),sg.Button('Cerrar')]
]
window=sg.Window('Probando',layout)

while True:
    event,values=window.read()
    if event=='Probar':
        window.disable()
        arch=sg.popup_get_file('ingrese archivo')
        print(arch)
        f=open(arch,'r')
        for line in f:
            print(line)
        window.enable()
    elif event=='Carpeta':
        window.disable()
        carp=sg.popup_get_folder('ingrese carpeta')
        print(carp)
        window.enable()
    else:
        break