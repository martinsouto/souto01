tam = ['im1 4,14', 'im2 13,15', 'im3 6,34', 'im4 410,134']
lis1=[] 
lis2=[]
num=int(input('Ingrese un valor'))
for i in tam:
    name,space,coord=i.partition(' ')
    x=int(coord.split(',')[0])
    coord=coord.split(',')
    tupla=(int(coord[0]),int(coord[1]))
    if x>num:       
        lis1.extend([name,tupla])
    else:       
        lis2.extend([name,tupla])
print(lis1)
print(lis2)

