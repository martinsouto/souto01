import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import time
import json

#La estructura de datos que elegi es un diccionario donde las claves son el nombre de usuario de los jugadores,los valores son listas que tienen el juego que jugó
# y la hora a la que lo hizo, esto esta dentro de otra lista. Esto es para que si un mismo usuario vuelve a jugar se guardé el nuevojuego que jugó sin borrar el anterior

# utilizo un archivo de tipo json ya que me resultan ordenados, fáciles de manejar y me permiten guardar la estructura donde estan almacenados los usuarios 

def guardar_datos(nombre, juego_hora):
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

def main(args):
	nombre=sg.popup_get_text('Ingrese nombre de usuario')
	
	lis_juegos=['Ahorcado','Ta Te Ti','Otello',]

	layout=[
    [sg.Text('Elija el juego que quiere jugar')],
    [sg.Listbox(values=lis_juegos,size=(40,4),key='lis_')],
    [sg.Button('Jugar'),sg.Button('Salir')]
	]
	window=sg.Window('Juegos',layout)

	while True:
		event,values=window.read()
		if event=='Jugar':
			juego_hora=[values['lis_'][0],time.asctime()]
			guardar_datos(nombre,juego_hora)
			window.Hide()
			if values['lis_'][0]=='Ahorcado':
				hangman.main()
			elif values['lis_'][0]=='Ta Te Ti':
				tictactoeModificado.main()
			elif values['lis_'][0]=='Otello':
				reversegam.main()
			window.UnHide()
		else:
			break
	window.close()
		
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
