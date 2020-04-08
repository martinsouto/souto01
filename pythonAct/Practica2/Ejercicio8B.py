palabra=input('Ingrese palabra')
ct=set(palabra)
for letra in ct:    
    print('La letra '+letra+' aparece '+str(palabra.count(letra))+' veces')    
