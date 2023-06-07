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
    return p_value


ttest_inicial = t_test(rendimiento_inicial)
ttest_primer =  t_test(rendimiento_primer_cambio)
ttest_segundo = t_test(rendimiento_segundo_cambio)

### --- COMPARACION --- ###

# funcion: ttest_ind: hace una prueba de hipotesis t entre dos muestras independientes
# y deteermina si las medias son significativamente diferentes
# entrada: muestra1, muestra2
# salida: estadistica de prueba (diferencia entre la media y el valor de referencia) y valor p


# PRIMER CAMBIO VS CAMBIO INICIAL
t_stat_pi, valor_p_pi = stats.ttest_ind(a=rendimiento_primer_cambio, b=rendimiento_inicial, nan_policy='omit',
                                        alternative='greater')

# SEGUNDO CAMBIO VS INICIAL
t_stat_is, valor_p_si = stats.ttest_ind(a=rendimiento_segundo_cambio, b=rendimiento_inicial, nan_policy='omit',
                                        alternative='greater')

# SEGUNDO CAMBIO VS PRIMER CAMBIO
t_stat_ps, valor_p_sp = stats.ttest_ind(a=rendimiento_segundo_cambio, b=rendimiento_primer_cambio, nan_policy='omit',
                                        alternative='greater')

print("2.1")
print("Hipótesis: \n h0 (nula): miu=70 \n h1 (alternativa): miu>=70")
print("---------Valores P obtenidos para comprobación de rendimientos---------")
print("Inicial:", ttest_inicial)
print("Primer Cambio:", ttest_primer)
print("Segundo Cambio:", ttest_segundo)
print("---------Valores P obtenidos para comparación de rendimientos---------")
print("Primer cambio e inicial:", valor_p_pi)
print("Segundo cambio e inicial:", valor_p_si)
print("Segundo Cambio y primer cambio:", valor_p_sp)

################## 2.2 ##################

### --- METODO MAXIMA VEROSIMILITUD --- ###
# METODO ANALÍTICO
# se crea una función para el cálculo de la desviación estándar por medio de la función de
# verosimilitud de una distribución normal
# entrada: (array) rendimiento
# salida: desviación estándar
def mle_desvesta(rendimiento):
    sumatoria = 0
    promedio = np.mean(rendimiento)
    for xi in rendimiento:
        sumatoria = sumatoria + (xi - promedio) ** 2
    varianza = (1 / len(rendimiento)) * sumatoria
    return math.sqrt(varianza)

desvesta_analitica_inicial = mle_desvesta(rendimiento_inicial)
desvesta_analitica_primer = mle_desvesta(rendimiento_primer_cambio)
desvesta_analitica_segundo = mle_desvesta(rendimiento_segundo_cambio)

# METODO EMPÍRICO
# se utiliza la función de scipy stats fit , la cual retorna la desviación de estándar de un conjunto de datos
# entrada: rendimiento (array), loc (media muestral)
# salida: _, desviación estándar
_, std_inicial = stats.norm.fit(rendimiento_inicial, loc=np.mean(rendimiento_inicial))
_, std_primer = stats.norm.fit(rendimiento_primer_cambio, loc=np.mean(rendimiento_primer_cambio))
_, std_segundo = stats.norm.fit(rendimiento_segundo_cambio, loc=np.mean(rendimiento_segundo_cambio))

# ERROR ENTRE METODO ANALITICO Y EMPIRICO
def error_std(std_a, std_e):
    resta = abs(std_a - std_e)
    div = resta/std_a
    return div*100

error_inicial = error_std(desvesta_analitica_inicial, std_inicial)
error_primer = error_std(desvesta_analitica_primer, std_primer)
error_segundo = error_std(desvesta_analitica_segundo, std_segundo)


print("\n\n2.2")
print("----------------------Desviación Estándar Inicial----------------------")
print("Analítica:", desvesta_analitica_inicial)
print("Empírica:", std_inicial)
print("Error:", error_inicial, "%")
print("-------------------Desviación Estándar Primer Cambio-------------------")
print("Analítica:", desvesta_analitica_primer)
print("Empírica:", std_primer)
print("Error:", error_primer, "%")
print("------------------Desviación Estándar Segundo Cambio-------------------")
print("Analítica:", desvesta_analitica_segundo)
print("Empírica:", std_segundo)
print("Error:", error_segundo, "%")