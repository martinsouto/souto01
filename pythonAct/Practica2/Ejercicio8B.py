palabra=input('Ingrese palabra')
ct=set(palabra)
for letra in ct:
    cont=0
    for i in palabra: 
        if letra==i:
            cont+=1
    print('La letra '+letra+' aparece '+str(cont)+' veces')    
