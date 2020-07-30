from pattern.text.es import verbs, tag, spelling, lexicon, parse, split
import string

def clasificar(palabra,clases_validas):
    """
    """
    aux = parse(palabra).split()[0][0][2]
    if aux in clases_validas:
        return True
    else:
        return False

def es_valida(palabra,dificultad):
    """
    """
    clases_validas=['B-ADJP','B-VP'] #'B-ADJP': adjetivo Parse /// 'B-VP': verbo Parse
    if (not palabra.lower() in verbs):
        if (not palabra.lower() in spelling):
            if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                ok=False
            else:
                ok=True
        else:
            ok=True
    else:
        ok=True
    if (ok==True):
        if (dificultad == '-FACIL-'):
            return True
        else:
            return clasificar(palabra,clases_validas)