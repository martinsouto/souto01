import os

arch=open('Archivos_7\coordenadas.txt','r')

x=arch.readline()
while x!='':
    lis_coords=x.split(',')
    print(lis_coords[0])
    print(lis_coords[1])
    if (lis_coords[1]=='2'):
        print('hola')
    x=arch.readline()
arch.close()

print('-'*50)
arch=open('Archivos_7\coordenadas.txt','r')
x=arch.read().splitlines()
for a in x:
    print(a)
arch.close()