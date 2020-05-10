import json
import time
nombre='martin'
juego='tic tac toe'
hora=time.asctime()
juego_hora=[juego,hora]
try:
    f=open('archivo.json','r')
    usuarios=json.load(f)
    if nombre in usuarios:
        usuarios[nombre].append(juego_hora)
    else:
        usuarios[nombre]=[juego_hora]
    f.close()
except:   
    usuarios={nombre:[juego_hora]}   
f=open('archivo.json','w')
json.dump(usuarios,f,indent=4)
f.close()
f=open('archivo.json','r')
data=json.load(f)
print(data)
f.close()