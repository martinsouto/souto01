imagenes=['im1','im2','im3']
lista_final=[]
for i in imagenes:
    ok=False
    while ok==False:
        coord_x=int(input('Ingrese coordenada x'))
        coord_y=int(input('Ingrese coordenada y'))
        if (coord_x!=coord_y):
            ok=True
            tupla=(coord_x,coord_y)
            print('Coordenadas ingresadas con éxito')
        else:
            print('Las coordenadas se repiten, ingreselas nuevamente')
    lista_final+=[i,tupla]
print(lista_final)