import numpy as np
import time


def leerDatos(ruta):
    return np.genfromtxt(ruta, delimiter=None)


def calcularProbabilidad(datosObtenidos, n):
    optimos = 0
    for fil in range(0, n):
        if (datosObtenidos[fil]['errorRelativo'] == 0):
            optimos += 1
    return optimos/n


def calcularVarianza(datosObtenidos, n):
    sum = 0
    for fil in range(0, n):
        sum += datosObtenidos[fil]['errorRelativo']**2
    return sum/n


def calcularTiempoHC(funcion, datosArray):
    inicio = time.time()
    s = funcion(datosArray)
    fin = time.time()
    s = s + (int(fin-inicio),)
    return s


def calcularTiempoHCILS(funcion, datosArray, iter):
    inicio = time.time()
    s = funcion(datosArray, iter)
    fin = time.time()
    s = s + (int(fin-inicio),)
    return s


def calcularTiempoSA(funcion, datosArray, t0, parada, f):
    inicio = time.time()
    s = funcion(datosArray, t0, parada, f)
    fin = time.time()
    s = s + (int(fin-inicio),)
    return s
