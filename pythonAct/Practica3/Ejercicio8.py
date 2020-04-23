def suma_todo(*args):
    if ((len(args))>30):
        return 'Se exedió el numero de elementos posibles'
    else:
        return sum(args)

def imprimo_dic(**kwargs):
    print(kwargs)



print(suma_todo(1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1))
print(suma_todo(3))
print(suma_todo(1,1))

