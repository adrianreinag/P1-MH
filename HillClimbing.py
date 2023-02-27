import random
import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import itertools


def evaluarSolucion(datos, solucion):
    longitud = 0
    for i in range(len(solucion)):
        longitud += datos[solucion[i - 1]][solucion[i]]
    return longitud

def obtenerMejorVecino(solucion, datos):
    # Obtención de los vecinos
    vecinos = []
    l = len(solucion)
    for i in range(l):
        for j in range(i+1, l):
            n = solucion.copy()
            n[i] = solucion[j]
            n[j] = solucion[i]
            vecinos.append(n)

    # Obtención del mejor vecino
    mejorVecino = vecinos[0]
    mejorLongitud = evaluarSolucion(datos, mejorVecino)
    for vecino in vecinos:
        longitud = evaluarSolucion(datos, vecino)
        if longitud < mejorLongitud:
            mejorLongitud = longitud
            mejorVecino = vecino
    return mejorVecino, mejorLongitud


def hillClimbing(datos):
    l = len(datos)
    # Creamos una solucion aleatoria
    ciudades = list(range(l))
    solucion = []
    for i in range(l):
        ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
        solucion.append(ciudad)
        ciudades.remove(ciudad)
    longitud = evaluarSolucion(datos, solucion)

    i = 0
    # print("Longitud de la ruta: ", longitud)
    # Obtenemos el mejor vecino hasta que no haya vecinos mejores
    vecino = obtenerMejorVecino(solucion, datos)
    while vecino[1] < longitud:
        solucion = vecino[0]
        longitud = vecino[1]
        # print("Longitud de la ruta: ", longitud)
        vecino = obtenerMejorVecino(solucion, datos)
        i += 1
    # Salto
    # Hacemos if para ver si hemos encontrado la mejor solucion y llamamos a la funcion
    # Hacemos return si no hemos encontrado mejor solucion
    return solucion, longitud, i


# def hillClimbingILS(datos):

#     vector = []

#     for i in range(0, 4):

#         l = len(datos)
#         # Creamos una solucion aleatoria
#         ciudades = list(range(l))
#         solucion = []
#         for i in range(l):
#             ciudad = ciudades[random.randint(0, len(ciudades) - 1)]
#             solucion.append(ciudad)
#             ciudades.remove(ciudad)
#         longitud = evaluarSolucion(datos, solucion)

#         # print("Longitud de la ruta: ", longitud)
#         # Obtenemos el mejor vecino hasta que no haya vecinos mejores
#         vecino = obtenerMejorVecino(solucion, datos)
#         while vecino[1] < longitud:
#             solucion = vecino[0]
#             longitud = vecino[1]
#             # print("Longitud de la ruta: ", longitud)
#             vecino = obtenerMejorVecino(solucion, datos)

#         mejor = vecino

#         vector[i] = vecino

#         if (mejor[1] > vecino[i][1]):

#             mejor[1] = vecino[i][1]

#         return mejor[1]


def main():

    datostxt = [
        {'nombre': 'five_d', 'nCiudades': 5, 'distanciaMinima': 19},
        {'nombre': 'p01_d', 'nCiudades': 15, 'distanciaMinima': 291},
        {'nombre': 'gr17_d', 'nCiudades': 17, 'distanciaMinima': 2085},
        {'nombre': 'fri26_d', 'nCiudades': 26, 'distanciaMinima': 937},
        {'nombre': 'dantzig42_d', 'nCiudades': 42, 'distanciaMinima': 699},
        {'nombre': 'att48_d', 'nCiudades': 48, 'distanciaMinima': 33523}
    ]

    datosObtenidosMedios = []

    i = 0
    n = 10

    for datotxt in datostxt:
        datosArray = leerDatos('./Datasets/' + datotxt['nombre'] + '.txt')

        datosObtenidos = []

        for fil in range(0, n):

            inicio = time.time()
            s = hillClimbing(datosArray)
            fin = time.time()

            datosObtenidos.append({'tiempoEjecucion': fin-inicio,
                                   'errorAbsoluto': s[1]-datotxt['distanciaMinima'],
                                   'errorRelativo': (s[1]-datotxt['distanciaMinima'])/s[1],
                                   'nIteraciones': s[2]})

        datosObtenidosMedios.append({'tiempoEjecucion': 0,
                                     'errorAbsoluto': 0,
                                     'errorRelativo': 0,
                                     'nIteraciones': 0})
        for fil in range(0, n):
            datosObtenidosMedios[i] = {'tiempoEjecucion': datosObtenidosMedios[i]['tiempoEjecucion']+datosObtenidos[fil]['tiempoEjecucion'],
                                       'errorAbsoluto': datosObtenidosMedios[i]['errorAbsoluto']+datosObtenidos[fil]['errorAbsoluto'],
                                       'errorRelativo': datosObtenidosMedios[i]['errorRelativo']+datosObtenidos[fil]['errorRelativo'],
                                       'nIteraciones': datosObtenidosMedios[i]['nIteraciones']+datosObtenidos[fil]['nIteraciones']}

        datosObtenidosMedios[i]['tiempoEjecucion'] = datosObtenidosMedios[i]['tiempoEjecucion']/n
        datosObtenidosMedios[i]['errorAbsoluto'] = datosObtenidosMedios[i]['errorAbsoluto']/n
        datosObtenidosMedios[i]['errorRelativo'] = datosObtenidosMedios[i]['errorRelativo']/n
        datosObtenidosMedios[i]['nIteraciones'] = datosObtenidosMedios[i]['nIteraciones']/n
        datosObtenidosMedios[i]['probabilidadOptimo'] = calcularProbabilidad(datosObtenidos, n)
        datosObtenidosMedios[i]['varianza'] = calcularVarianza(datosObtenidos, n)
        
        i += 1
            
    tiempoEjecucionPlot = []
    errorAbsolutoPlot = []
    errorRelativoPlot = []
    nIteracionesPlot = []
    probabilidadOptimoPlot = []
    varianzaPlot = []
    nCiudades = []

    for i in range(len(datosObtenidosMedios)):
        tiempoEjecucionPlot.append(datosObtenidosMedios[i]['tiempoEjecucion'])
        errorAbsolutoPlot.append(datosObtenidosMedios[i]['errorAbsoluto'])
        errorRelativoPlot.append(datosObtenidosMedios[i]['errorRelativo'])
        nIteracionesPlot.append(datosObtenidosMedios[i]['nIteraciones'])
        probabilidadOptimoPlot.append(datosObtenidosMedios[i]['probabilidadOptimo'])
        varianzaPlot.append(datosObtenidosMedios[i]['varianza'])
        nCiudades.append(datostxt[i]['nCiudades'])

    nCiudades_new = np.linspace(min(nCiudades), max(nCiudades), 100)

    f_tiempoEjecucionPlot = interp1d(nCiudades, tiempoEjecucionPlot, kind='cubic')
    plt.plot(nCiudades_new, f_tiempoEjecucionPlot(nCiudades_new))
    plt.plot(nCiudades, tiempoEjecucionPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Tiempo de ejecución por número de ciudades')
    plt.savefig('tiempoEjecucion.eps', format='eps')
    plt.show()

    f_errorAbsolutoPlot = interp1d(nCiudades, errorAbsolutoPlot, kind='cubic')
    plt.plot(nCiudades_new, f_errorAbsolutoPlot(nCiudades_new))
    plt.plot(nCiudades, errorAbsolutoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error absoluto')
    plt.title('Error absoluto por número de ciudades')
    plt.savefig('errorAbsoluto.eps', format='eps')
    plt.show()

    f_errorRelativoPlot = interp1d(nCiudades, errorRelativoPlot, kind='cubic')
    plt.plot(nCiudades_new, f_errorRelativoPlot(nCiudades_new))
    plt.plot(nCiudades, errorRelativoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error relativo')
    plt.title('Error relativo por número de ciudades')
    plt.savefig('errorRelativo.eps', format='eps')
    plt.show()

    f_nIteracionesPlot = interp1d(nCiudades, nIteracionesPlot, kind='cubic')
    plt.plot(nCiudades_new, f_nIteracionesPlot(nCiudades_new))
    plt.plot(nCiudades, nIteracionesPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Número de iteraciones')
    plt.title('Número de iteraciones por número de ciudades')
    plt.savefig('nIteraciones.eps', format='eps')
    plt.show()

    f_probabilidadOptimoPlot = interp1d(nCiudades, probabilidadOptimoPlot, kind='cubic')
    plt.plot(nCiudades_new, f_probabilidadOptimoPlot(nCiudades_new))
    plt.plot(nCiudades, probabilidadOptimoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Probabilidad de encontrar la solución óptima')
    plt.title('Probabilidad de encontrar la solución óptima por número de ciudades')
    plt.savefig('probabilidadOptimo.eps', format='eps')
    plt.show()

    f_varianzaPlot = interp1d(nCiudades, varianzaPlot, kind='cubic')
    plt.plot(nCiudades_new, f_varianzaPlot(nCiudades_new))
    plt.plot(nCiudades, varianzaPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Varianza')
    plt.title('Varianza por número de ciudades')
    plt.savefig('varianza.eps', format='eps')
    plt.show()
        
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

if __name__ == "__main__":
    main()
