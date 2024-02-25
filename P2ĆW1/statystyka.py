def srednia(lista):
    return sum(lista) / len(lista)

def mediana(lista):
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        return (lista[n//2 - 1] + lista[n//2]) / 2
    else:
        return lista[n//2]

def wariancja(lista):
    sred = srednia(lista)
    return sum((xi - sred) ** 2 for xi in lista) / len(lista)
