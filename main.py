import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd
import math

################## 2.1 ##################
# se establecen las hipotesis:
#       h0 (nula): miu=70
#       h1 (alternativa): miu>=70

# recopilación de datos durante 90 días:

ruta = 'Conjunto_datos_proyecto3.xlsx'
datos = pd.read_excel(ruta)
rendimiento_inicial = datos['Inicial'].to_numpy()
rendimiento_primer_cambio = datos['Primer_cambio'].to_numpy()
rendimiento_segundo_cambio = datos['Segundo_cambio'].to_numpy()


### --- COMPROBACION --- ###
# funcion: ttest_1samp: prueba de hipotesis t de una muestra, compara la media
#  con la hipotesis nula y determina si es significativamente diferente al valor de referencia
# entrada: a: rendimiennto, popmean: miu h0, nan_policy: omit, alternative: greater
# salida: estadistica de prueba, valor p

def t_test(rendimiento):
    media_muestral = np.mean(rendimiento)
    desviacion_estandar_muestral = np.std(rendimiento,
                                          ddof=1)  # ddof=1 para utilizar la fórmula de la desviación estándar muestral
    # a: rendimiennto, popmean: miu h0, nan_policy: omit, alternative: greater
    t_stat, p_value = stats.ttest_1samp(a=rendimiento, popmean=70, nan_policy='omit', alternative='greater')
    print(p_value)


### INICIAL ###
print("--------------------------------Inicial--------------------------------")
print(rendimiento_inicial)
t_test(rendimiento_inicial)

### PRIMER CAMBIO ###
print("-----------------------------Primer Cambio-----------------------------")
print(rendimiento_primer_cambio)
t_test(rendimiento_primer_cambio)

### SEGUNDO CAMBIO ###
print("----------------------------Segundo Cambio-----------------------------")
print(rendimiento_segundo_cambio)
t_test(rendimiento_segundo_cambio)

### --- COMPARACION --- ###

# funcion: ttest_ind: hace una prueba de hipotesis t entre dos muestras independientes
# y deteermina si las medias son significativamente diferentes
# entrada: muestra1, muestra2
# salida: estadistica de prueba (diferencia entre la media y el valor de referencia) y valor p


# INICIAL VS PRIMER CAMBIO
print("--------------------------------P VS I--------------------------------")
t_stat_ip, valor_p_ip = stats.ttest_ind(a=rendimiento_primer_cambio, b=rendimiento_inicial, nan_policy='omit',
                                        alternative='greater')
print(valor_p_ip)

# INICIAL VS SEGUNDO CAMBIO
print("--------------------------------S VS I--------------------------------")
t_stat_is, valor_p_is = stats.ttest_ind(a=rendimiento_segundo_cambio, b=rendimiento_inicial, nan_policy='omit',
                                        alternative='greater')
print(valor_p_is)

# PRIMER CAMBIO VS SEGUNDO CAMBIO
print("--------------------------------S VS P--------------------------------")
t_stat_ps, valor_p_ps = stats.ttest_ind(a=rendimiento_segundo_cambio, b=rendimiento_primer_cambio, nan_policy='omit',
                                        alternative='greater')
print(valor_p_ps)

################## 2.2 ##################

### --- METODO MAXIMA VEROSIMILITUD --- ###
# metodo analitico
# entrada: (array) rendimiento
# salida: desviación estándar
def mle_desvesta(rendimiento):
    sumatoria = 0
    promedio = np.mean(rendimiento)
    for xi in rendimiento:
        sumatoria = (xi - promedio) ** 2
    varianza = (1 / len(rendimiento)) * sumatoria
    return math.sqrt(varianza)

# metodo empírico

### INICIAL ###
print("----------------------Desviaciones Inicial----------------------")
print(mle_desvesta(rendimiento_inicial))
_, std_inicial = stats.norm.fit(rendimiento_inicial, loc=np.mean(rendimiento_inicial))
print(std_inicial)

### PRIMER CAMBIO ###
print("-------------------Desviaciones Primer Cambio-------------------")
print(mle_desvesta(rendimiento_primer_cambio))
_, std_primer = stats.norm.fit(rendimiento_primer_cambio, loc=np.mean(rendimiento_primer_cambio))
print(std_primer)

### SEGUNDO CAMBIO ###
print("------------------Desviaciones Segundo Cambio-------------------")
print(mle_desvesta(rendimiento_segundo_cambio))
_, std_segundo = stats.norm.fit(rendimiento_segundo_cambio, loc=np.mean(rendimiento_segundo_cambio))
print(std_segundo)