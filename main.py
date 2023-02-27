import HillClimbing as hc
import SimAnnealing as sa
import funciones as f
import matplotlib.pyplot as plt


def obtenerDatosHC(datostxt, n):
    datosObtenidosMedios = []

    i = 0

    for datotxt in datostxt:
        datosArray = f.leerDatos('./Datasets/' + datotxt['nombre'] + '.txt')

        datosObtenidos = []

        for fil in range(0, n):

            s = f.calcularTiempoHC(hc.hillClimbing, datosArray)

            datosObtenidos.append({'tiempoEjecucion': s[3],
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
        datosObtenidosMedios[i]['probabilidadOptimo'] = f.calcularProbabilidad(datosObtenidos, n)
        datosObtenidosMedios[i]['varianza'] = f.calcularVarianza(datosObtenidos, n)
        
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

    plt.plot(nCiudades, tiempoEjecucionPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Tiempo de ejecución por número de ciudades')
    plt.savefig('tiempoEjecucionHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, errorAbsolutoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error absoluto')
    plt.title('Error absoluto por número de ciudades')
    plt.savefig('errorAbsolutoHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, errorRelativoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error relativo')
    plt.title('Error relativo por número de ciudades')
    plt.savefig('errorRelativoHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, nIteracionesPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Número de iteraciones')
    plt.title('Número de iteraciones por número de ciudades')
    plt.savefig('nIteracionesHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, probabilidadOptimoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Probabilidad de encontrar la solución óptima')
    plt.title('Probabilidad de encontrar la solución óptima por número de ciudades')
    plt.savefig('probabilidadOptimoHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, varianzaPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Varianza')
    plt.title('Varianza por número de ciudades')
    plt.savefig('varianzaHC.svg', format='svg')
    plt.show()

    return tiempoEjecucionPlot, errorAbsolutoPlot, errorRelativoPlot, nIteracionesPlot, probabilidadOptimoPlot, varianzaPlot, nCiudades

def obtenerDatosHCILS(datostxt, n, iter):
    datosObtenidosMedios = []

    i = 0

    for datotxt in datostxt:
        datosArray = f.leerDatos('./Datasets/' + datotxt['nombre'] + '.txt')

        datosObtenidos = []

        for fil in range(0, n):

            s = f.calcularTiempoHCILS(hc.hillClimbingILS, datosArray, iter)

            datosObtenidos.append({'tiempoEjecucion': s[3],
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
        datosObtenidosMedios[i]['probabilidadOptimo'] = f.calcularProbabilidad(datosObtenidos, n)
        datosObtenidosMedios[i]['varianza'] = f.calcularVarianza(datosObtenidos, n)
        
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


    plt.plot(nCiudades, tiempoEjecucionPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Tiempo de ejecución por número de ciudades')
    plt.savefig('tiempoEjecucionHCILS.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, errorAbsolutoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error absoluto')
    plt.title('Error absoluto por número de ciudades')
    plt.savefig('errorAbsolutoHCILS.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, errorRelativoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error relativo')
    plt.title('Error relativo por número de ciudades')
    plt.savefig('errorRelativoHCILS.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, nIteracionesPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Número de iteraciones')
    plt.title('Número de iteraciones por número de ciudades')
    plt.savefig('nIteracionesHCILS.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, probabilidadOptimoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Probabilidad de encontrar la solución óptima')
    plt.title('Probabilidad de encontrar la solución óptima por número de ciudades')
    plt.savefig('probabilidadOptimoHCILS.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, varianzaPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Varianza')
    plt.title('Varianza por número de ciudades')
    plt.savefig('varianzaHCILS.svg', format='svg')
    plt.show()

    return tiempoEjecucionPlot, errorAbsolutoPlot, errorRelativoPlot, nIteracionesPlot, probabilidadOptimoPlot, varianzaPlot, nCiudades

def comparacionHC(sHC, sHCILS):
    plt.plot(sHC[6], sHC[0], label="HC")
    plt.plot(sHCILS[6], sHCILS[0], label="HCILS")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Tiempo de ejecución por número de ciudades')
    plt.savefig('tiempoEjecucionComparativaHC.svg', format='svg')
    plt.show()

    plt.plot(sHC[6], sHC[1], label="HC")
    plt.plot(sHCILS[6], sHCILS[1], label="HCILS")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error absoluto')
    plt.title('Error absoluto por número de ciudades')
    plt.savefig('errorAbsolutoComparativaHC.svg', format='svg')
    plt.show()

    plt.plot(sHC[6], sHC[2], label="HC")
    plt.plot(sHCILS[6], sHCILS[2], label="HCILS")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error relativo')
    plt.title('Error relativo por número de ciudades')
    plt.savefig('errorRelativoComparativaHC.svg', format='svg')
    plt.show()

    plt.plot(sHC[6], sHC[3], label="HC")
    plt.plot(sHCILS[6], sHCILS[3], label="HCILS")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Número de iteraciones')
    plt.title('Número de iteraciones por número de ciudades')
    plt.savefig('nIteracionesComparativaHC.svg', format='svg')
    plt.show()

    plt.plot(sHC[6], sHC[4], label="HC")
    plt.plot(sHCILS[6], sHCILS[4], label="HCILS")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Probabilidad de encontrar la solución óptima')
    plt.title('Probabilidad de encontrar la solución óptima por número de ciudades')
    plt.savefig('probabilidadOptimoComparativaHC.svg', format='svg')
    plt.show()

    plt.plot(sHC[6], sHC[5], label="HC")
    plt.plot(sHCILS[6], sHCILS[5], label="HCILS")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Varianza')
    plt.title('Varianza por número de ciudades')
    plt.savefig('varianzaComparativaHC.svg', format='svg')
    plt.show()

def obtenerDatosSA(datostxt, n, t0, parada, funcion):
    datosObtenidosMedios = []

    i = 0

    for datotxt in datostxt:
        datosArray = f.leerDatos('./Datasets/' + datotxt['nombre'] + '.txt')

        datosObtenidos = []

        for fil in range(0, n):

            s = f.calcularTiempoSA(sa.simAnnealing, datosArray, t0, parada, funcion)

            datosObtenidos.append({'tiempoEjecucion': s[3],
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
        datosObtenidosMedios[i]['probabilidadOptimo'] = f.calcularProbabilidad(datosObtenidos, n)
        datosObtenidosMedios[i]['varianza'] = f.calcularVarianza(datosObtenidos, n)
        
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

    plt.plot(nCiudades, tiempoEjecucionPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Tiempo de ejecución por número de ciudades')
    plt.savefig('tiempoEjecucionHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, errorAbsolutoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error absoluto')
    plt.title('Error absoluto por número de ciudades')
    plt.savefig('errorAbsolutoHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, errorRelativoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error relativo')
    plt.title('Error relativo por número de ciudades')
    plt.savefig('errorRelativoHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, nIteracionesPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Número de iteraciones')
    plt.title('Número de iteraciones por número de ciudades')
    plt.savefig('nIteracionesHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, probabilidadOptimoPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Probabilidad de encontrar la solución óptima')
    plt.title('Probabilidad de encontrar la solución óptima por número de ciudades')
    plt.savefig('probabilidadOptimoHC.svg', format='svg')
    plt.show()

    plt.plot(nCiudades, varianzaPlot)
    plt.xlabel('Número de ciudades')
    plt.ylabel('Varianza')
    plt.title('Varianza por número de ciudades')
    plt.savefig('varianzaHC.svg', format='svg')
    plt.show()

    return tiempoEjecucionPlot, errorAbsolutoPlot, errorRelativoPlot, nIteracionesPlot, probabilidadOptimoPlot, varianzaPlot, nCiudades

def comparacionSA(sSA, sSALog, sSAGeo):
    plt.plot(sSA[6], sSA[0], label="SA")
    plt.plot(sSALog[6], sSALog[0], label="SALog")
    plt.plot(sSAGeo[6], sSAGeo[0], label="SAGeo")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Tiempo de ejecución')
    plt.title('Tiempo de ejecución por número de ciudades')
    plt.savefig('tiempoEjecucionComparativaSA.svg', format='svg')
    plt.show()

    plt.plot(sSA[6], sSA[1], label="SA")
    plt.plot(sSALog[6], sSALog[0], label="SALog")
    plt.plot(sSAGeo[6], sSAGeo[0], label="SAGeo")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error absoluto')
    plt.title('Error absoluto por número de ciudades')
    plt.savefig('errorAbsolutoComparativaSA.svg', format='svg')
    plt.show()

    plt.plot(sSA[6], sSA[2], label="SA")
    plt.plot(sSALog[6], sSALog[0], label="SALog")
    plt.plot(sSAGeo[6], sSAGeo[0], label="SAGeo")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Error relativo')
    plt.title('Error relativo por número de ciudades')
    plt.savefig('errorRelativoComparativaSA.svg', format='svg')
    plt.show()

    plt.plot(sSA[6], sSA[3], label="SA")
    plt.plot(sSALog[6], sSALog[0], label="SALog")
    plt.plot(sSAGeo[6], sSAGeo[0], label="SAGeo")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Número de iteraciones')
    plt.title('Número de iteraciones por número de ciudades')
    plt.savefig('nIteracionesComparativaSA.svg', format='svg')
    plt.show()

    plt.plot(sSA[6], sSA[4], label="SA")
    plt.plot(sSALog[6], sSALog[0], label="SALog")
    plt.plot(sSAGeo[6], sSAGeo[0], label="SAGeo")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Probabilidad de encontrar la solución óptima')
    plt.title('Probabilidad de encontrar la solución óptima por número de ciudades')
    plt.savefig('probabilidadOptimoComparativaSA.svg', format='svg')
    plt.show()

    plt.plot(sSA[6], sSA[5], label="SA")
    plt.plot(sSALog[6], sSALog[0], label="SALog")
    plt.plot(sSAGeo[6], sSAGeo[0], label="SAGeo")
    plt.legend()
    plt.xlabel('Número de ciudades')
    plt.ylabel('Varianza')
    plt.title('Varianza por número de ciudades')
    plt.savefig('varianzaComparativaSA.svg', format='svg')
    plt.show()


def main():
    datostxt = [
        {'nombre': 'five_d', 'nCiudades': 5, 'distanciaMinima': 19},
        {'nombre': 'p01_d', 'nCiudades': 15, 'distanciaMinima': 291},
        {'nombre': 'gr17_d', 'nCiudades': 17, 'distanciaMinima': 2085},
        {'nombre': 'fri26_d', 'nCiudades': 26, 'distanciaMinima': 937},
        {'nombre': 'dantzig42_d', 'nCiudades': 42, 'distanciaMinima': 699},
        {'nombre': 'att48_d', 'nCiudades': 48, 'distanciaMinima': 33523}
    ]

    n = 2

    # sHC = obtenerDatosHC(datostxt, n)

    # sHCILS = obtenerDatosHCILS(datostxt, n, 5)

    # comparacionHC(sHC, sHCILS)

    sSA = obtenerDatosSA(datostxt, n, 10, 0.05, 1)

    sSALog = obtenerDatosSA(datostxt, n, 10, 2, 2)

    sSAGeo = obtenerDatosSA(datostxt, n, 10, 0.05, 3)

    comparacionSA(sSA, sSALog, sSAGeo)

if __name__ == "__main__":
    main()