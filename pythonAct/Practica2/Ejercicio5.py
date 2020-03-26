x=input('Menú de opciones para la lista de números a ingresar: \n1: ingresar números \n2: ordenar números \n3: calcular el máximo \n4: calcular el mínimo \n5: calcular el promedio \n0: para terminar')
x=int(x)
vacio=[]
lis=[]
while x!=0:
    if x==1:
        num=int(input('Ingrese numero'))
        n=[num]
        lis.extend(n)
        otro=input('Desea agregar otro numero')
        while otro=='si':
            num=[input('Ingrese numero')]
            lis.extend(num)
            otro=input('Desea agregar otro numero')
    elif lis!=vacio:
        if x==2:
            lis.sort()
            print('Lista ordenada con exito')
            print(lis)
        elif x==3:
            print(max(lis))
        elif x==4:
            print(min(lis))
        elif x==5:
            print(sum(lis)/len(lis))
        else:
            print('Numero ingresado no valido')
    else:
        print('La lista esta vacia')
    x=input('Menú de opciones para la lista de números a ingresar: \n1: ingresar números \n2: ordenar números \n3: calcular el máximo \n4: calcular el mínimo \n5: calcular el promedio \n0: para terminar')
    x=int(x)