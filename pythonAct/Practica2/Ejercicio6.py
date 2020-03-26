x=int(input('Ingrsar num 1'))
y=int(input('Ingresar num 2'))
op=input('Que operacion desea hacer \n + \n - \n * \n /')
if op=='+':
    print(x+y)
elif op=='-':
    print(x-y)
elif op=='*':
    print(x*y)
elif op=='/':
    print(x/y)
else:
    print('Operacion no valida')
