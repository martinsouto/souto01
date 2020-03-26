frase='hola hola chau hola CHau HoLa'
frase=frase.lower()
lista=frase.split(' ')
lista_n=[]
for s in lista:
	if s not in lista_n:
		lista_n=lista_n+[s]
print(lista_n)
