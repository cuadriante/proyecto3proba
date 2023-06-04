import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pandas as pd

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
        desviacion_estandar_muestral = np.std(rendimiento, ddof=1)  # ddof=1 para utilizar la fórmula de la desviación estándar muestral
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
print("--------------------------------I VS P--------------------------------")
t_stat_ip, valor_p_ip = stats.ttest_ind(a=rendimiento_inicial, b=rendimiento_primer_cambio, nan_policy='omit', alternative='greater')
print(valor_p_ip)

# PRIMER CAMBIO VS SEGUNDO CAMBIO
print("--------------------------------P VS S--------------------------------")
t_stat_ps, valor_p_ps = stats.ttest_ind(a=rendimiento_primer_cambio, b=rendimiento_segundo_cambio, nan_policy='omit', alternative='greater')
print(valor_p_ps)
# INICIAL VS SEGUNDO CAMBIO
print("--------------------------------I VS S--------------------------------")
t_stat_is, valor_p_is = stats.ttest_ind(a=rendimiento_inicial, b=rendimiento_segundo_cambio, nan_policy='omit', alternative='greater')
print(valor_p_is)







