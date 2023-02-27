import random
import math


def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud


def obtenerVecino(solucion, datos):
    # Obtención de los vecinos
    vecinos = []
    l = len(solucion)
    for i in range(l):
        for j in range(i+1, l):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    # Obtengo un vecino aleatorio
    vecino = vecinos[random.randint(0, len(vecinos) - 1)]
    longitud = evaluarSolucion(datos, vecino)

    return vecino, longitud


def simAnnealing(datos, t0, parada, funcion):
    t = t0
    l = len(datos)
    # Creamos una solucion aleatoria
    ciudades = list(range(l))
    solucion = []
    for i in range(l):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        solucion.append(ciudad)
        ciudades.remove(ciudad)
    longitud = evaluarSolucion(datos, solucion)

    it = 0
    while t > parada:
        # Obtenemos un vecino al azar
        vecino = obtenerVecino(solucion, datos)
        incremento = vecino[1]-longitud

        if incremento < 0:
            longitud = vecino[1]
            solucion = vecino[0]
        elif random.random() < math.exp(-abs(incremento) / t):
            longitud = vecino[1]
            solucion = vecino[0]

        it += 1
        if(funcion==1):
            t = enfriamiento(t)
        elif(funcion==2):
            t = enfriamientoLog(t0, it)
        elif(funcion==3):
            t = enfriamientoGeo(t0, it)

    return solucion, longitud, it


def enfriamiento(t):
    a = 0.99
    return a*t

def enfriamientoLog(t0, it):
    a = 0.99
    return (a*t0)/(math.log(1+it))

def enfriamientoGeo(t0, it):
    a = 0.99
    return t0*a**it