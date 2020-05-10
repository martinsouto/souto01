import PySimpleGUI as sg

tablero1=[
    [sg.Button('',size=(3,3)) for col in range(10)]for fil in range(10)
]
tablero2=[[sg.Button('a'),sg.Button('b'),sg.Button('c'),sg.Button('d'),sg.Button('e')]]
final=[[sg.Button('ok')]]
layout=tablero1+tablero2+final

window=sg.Window('Tableros',layout,size=(40,40))

while True:
    event,values=window.read()
    if event=='ok':
        break
window.close()