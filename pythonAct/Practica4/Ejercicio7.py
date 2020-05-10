import PySimpleGUI as sg


archivo_coordenadas=sg.popup_get_file('Ingrese archivo de coordenadas')
archivo_colores=sg.popup_get_file('Ingrese archivo de colores')

layout=[
    [sg.Graph((400,400),(0,0),(400,400),background_color='white',enable_events=True,key='graph')],
    [sg.Button('Draw'),sg.Button('Save'),sg.Button('Close')],
]
window=sg.Window('Dibujo',layout,finalize=True)
graph=window['graph']

arch_coords=open(archivo_coordenadas,'r')
coords=arch_coords.read().splitlines()
arch_colors=open(archivo_colores,'r')
colors=arch_colors.read().splitlines()

while True:
    event,values=window.read()
    if event=='Draw':
        cont=0
        for color in colors:
            print(color)
            print(coords[cont])
            lis_coords=coords[cont].split(',')
            point=graph.draw_point((int(lis_coords[0]),int(lis_coords[1])),10,color=color)
            cont+=1
    elif event=='Save':
            window.disable()
            carpeta=sg.popup_get_folder('Seleccione carpeta')
            print(carpeta)
            f=open(carpeta+'\\Archivo_nuevo.txt','w')
            con=0
            for color in colors:
                f.write(coords[con]+' '+color+'\n')
                con+=1
            f.close()
            window.enable()
    else:
        break

arch_coords.close()
arch_colors.close()

