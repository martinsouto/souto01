import functools

def procesar(op,lis_args=[],lis_nom=[]):
    if (lis_args==[]):
        print('no se pasaron operandos')
    else:
        operaciones={'+':(lambda x,y:x+y),'*':(lambda x,y:x*y)}
        res=functools.reduce(operaciones[op],lis_args)
        print(res)
        if (lis_nom!=[]):
            print('datos de la persona que solicitó la operacion:')
            for i in lis_nom:
                print(i)
        else:
            print('no hay datos de la persona que solicitó la operación')

procesar('+',[3,3],['martin','souto'])
print('-'*30)
procesar('*',[2,3,3])
