palabra=input('Ingresar palabra')
no=''
for letra in palabra:
    if letra not in no:
        print('la letra '+letra+' aparece '+str(palabra.count(letra))+' veces')
    no=no+letra