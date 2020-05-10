import PySimpleGUI as sg

layout=[
    [sg.Graph((400,400),(0,0),(400,400),background_color='white',enable_events=True,key='graph')],
    [sg.Button('Draw'),sg.Button('Close')],
]

window=sg.Window('Dibujo',layout,finalize=True)
graph=window['graph']


while True:
    event,values=window.read()
    if event=='Draw':
        point= graph.draw_point((75,75),10,color='black')
        print(values)

    else:
        break

window.close()