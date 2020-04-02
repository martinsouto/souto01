import random

def determino_palabra():
    palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
    tema = int(input('Elige un tema:\n 1: animales\n 2: colores\n 3: comidas\n '))
    pal = palabras[tema][random.randrange(len(palabras[tema]))]
    return pal

def armo_estructura(pal):
    pal_separada = []
    for y in pal:
	    pal_separada.append(['_ '])
    print ('- '*len(pal))
    return pal_separada

def si_gane(letras_ad, pal):
    if letras_ad==len(pal):
        print('Ganaste')
        return False
    else:
        return True

def si_perdi(partes_c, pal):
    if partes_c==3:
        print('Perdiste!. La palabra era:', pal)
        return False
    else:
        return True

def un_intento(pal, pal_separada, ahorcado, cantidades):
    letra = input('Ingresa una letra: ').lower()
    if letra in pal:				
        for pos in range(len (pal)):			
            if pal[pos] == letra:
                pal_separada[pos] = letra				
                cantidades['letras adivinadas'] = cantidades['letras adivinadas'] + 1			
        pal_imprime = ''
        for y in pal_separada:
            pal_imprime = pal_imprime + y[0]
        print (pal_imprime)
        return si_gane(cantidades['letras adivinadas'], pal)	
    else:
        cantidades['partes cuerpo']=cantidades['partes cuerpo'] + 1
        for x in range(cantidades['partes cuerpo']):
            print (ahorcado[x])
        return si_perdi(cantidades['partes cuerpo'], pal)

def jugar():
    pal=determino_palabra()
    pal_separada=armo_estructura(pal)
    ahorcado = [' O ', '/|\\','/ \\']
    cantidades={'partes cuerpo':0,'letras adivinadas':0}
    sigue=True
    while sigue:
        sigue= un_intento(pal, pal_separada, ahorcado, cantidades)

devuelta='si'
while devuelta=='si':
    jugar()
    devuelta=input('Quiere jugar devuelta?(si o no)')