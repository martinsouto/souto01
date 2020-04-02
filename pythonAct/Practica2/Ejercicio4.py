import random
puntos=0
preguntas = [['Buenos Aires limita con Santiago del Estero', 'no'], ['Jujuy limita con Bolivia', 'si'], ['San Juan limita con Misiones', 'no']]
while (preguntas!=[]):
    al=random.randint(0,len(preguntas)-1)
    #tambien podria haber puesto random.randrange(len(preguntas))
    print(preguntas[al][0])
    x=input('Responda si o no').lower()
    if x==preguntas[al][1]:
        print('Respuesta correcta')
        puntos=puntos+1
    else:
        print('Respuesta incorrecta')
    del preguntas[al]
print('Resultado: '+ str(puntos) +' puntos')

