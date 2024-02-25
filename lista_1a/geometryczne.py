import math

def pole_prostokata(a, b):
    return a * b

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_kola(r):
    return math.pi * r**2

def objetosc_szescianu(a):
    return a**3

def objetosc_walca(r, h):
    return math.pi * r**2 * h

def objetosc_stozka(r, h):
    return (1/3) * math.pi * r**2 * h
