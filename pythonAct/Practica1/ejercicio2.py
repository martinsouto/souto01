frase=input('ingresar frase: ')
busqueda=input('ingrese una palabra de la frase: ')
frase=frase.lower()
busqueda=busqueda.lower()
lista=frase.split(' ')
cont=0
for s in lista:
	if busqueda in s:
		cont=cont+1
print(cont)

