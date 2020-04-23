def impresion_enumerate(*args):
    for count,nom in enumerate(args):
        print(count, nom)

impresion_enumerate('martin','federico','juan')