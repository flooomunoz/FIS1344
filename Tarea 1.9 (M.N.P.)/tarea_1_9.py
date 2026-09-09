# FIS 1344-1 Tarea 1.9
# Florencia Antonia Muñoz Aburto 21.600.645-3

import numpy as np
import matplotlib.pyplot as mlt

# Posiciones del enunciado medidas en cm
datos_1_cm = np.array([0.9, 2.0, 3.6, 5.6, 8.0, 10.9, 14.2, 18.0])
datos_7_cm = np.array([0.3, 1.7, 4.1, 5.7, 8.5, 10.7, 13.6, 17.2])

# Convertimos la incertidumbre: 4mm = 0.4 cm
incertidumbre_cm = 4 / 10

# Enumeramos del 1 al 8 las mediciones
numero_medicion = np.arange(1, len(datos_1_cm) + 1)
# len(datos_1_cm) devuelve la cantidad de posiciones: 8.
# np.arange excluye el limite final; por eso usamos 8 + 1.
# Obtenemos los numeros del 1 al 8, correspondientes a las mediciones.

# Ajustamos una parabola a las posiciones del primer estudiante
coeficientes_1 = np.polyfit(numero_medicion, datos_1_cm, 2)

# Calculamos las posiciones que predice esa parabola
posiciones_ajustadas_1_cm = np.polyval(coeficientes_1, numero_medicion)

# Ajustamos una parabola a las posiciones del segundo estudiante
coeficientes_7 = np.polyfit(numero_medicion, datos_7_cm, 2)

# Calculamos las posiciones que predice esa segunda parabola
posiciones_ajustadas_7_cm = np.polyval(coeficientes_7, numero_medicion)

# Mostramos los coeficientes de ambas parabolas para revisarlos
print("Coeficientes del primer conjunto:", coeficientes_1)
print("Coeficientes del segundo conjunto:", coeficientes_7)

# Calculamos los residuos: posicion medida menos posicion ajustada
residuos_1_cm = datos_1_cm - posiciones_ajustadas_1_cm
residuos_7_cm = datos_7_cm - posiciones_ajustadas_7_cm


# Sumamos los cuadrados de los residuos de cada conjunto
suma_residuos_1 = np.sum(residuos_1_cm ** 2)
suma_residuos_7 = np.sum(residuos_7_cm ** 2)


# Calculamos la variacion total respecto de la media de cada conjunto
suma_total_1 = np.sum((datos_1_cm - np.mean(datos_1_cm)) ** 2)
suma_total_7 = np.sum((datos_7_cm - np.mean(datos_7_cm)) ** 2)

# Calculamos el coeficiente de determinacion R al cuadrado
r2_1 = 1 - suma_residuos_1 / suma_total_1
r2_7 = 1 - suma_residuos_7 / suma_total_7

# Mostramos ocho decimales para distinguir valores muy cercanos a 1
print(f"R cuadrado del primer conjunto: {r2_1:.8f}")
print(f"R cuadrado del segundo conjunto: {r2_7:.8f}")

# Generamos puntos intermedios para dibujar las parabolas suavemente
# Estos puntos sirven para las curvas; no son nuevas mediciones
mediciones_curva = np.linspace(1, len(datos_1_cm), 200)

# Creamos dos graficos con las mismas escalas para compararlos
figura, ejes = mlt.subplots(
    1, 2, figsize=(12, 5), sharex=True, sharey=True
)

# Dibujamos las posiciones y barras de error del primer estudiante
ejes[0].errorbar(
    numero_medicion, datos_1_cm, yerr=incertidumbre_cm,
    fmt="o", color="purple", capsize=4,
    label="Posiciones con incertidumbre"
)

# Dibujamos la parabola ajustada al primer conjunto
ejes[0].plot(
    mediciones_curva, np.polyval(coeficientes_1, mediciones_curva),
    color="purple", linestyle="--", label="Ajuste cuadratico"
)
ejes[0].set_title(f"Primer conjunto: R² = {r2_1:.8f}")

# Dibujamos las posiciones y barras de error del segundo estudiante
ejes[1].errorbar(
    numero_medicion, datos_7_cm, yerr=incertidumbre_cm,
    fmt="o", color="darkorange", capsize=4,
    label="Posiciones con incertidumbre"
)

# Dibujamos la parabola ajustada al segundo conjunto
ejes[1].plot(
    mediciones_curva, np.polyval(coeficientes_7, mediciones_curva),
    color="darkorange", linestyle="--", label="Ajuste cuadratico"
)
ejes[1].set_title(f"Segundo conjunto: R² = {r2_7:.8f}")

# Agregamos nombres de ejes, escala, cuadricula y leyenda a ambos graficos
for eje in ejes:
    eje.set_xlabel("Numero de medicion (intervalos iguales)")
    eje.set_ylabel("Posicion (cm)")
    eje.set_xticks(numero_medicion)
    eje.set_ylim(-1, 19)
    eje.grid(alpha=0.3)
    eje.legend()

# Ajustamos los espacios para evitar que se superpongan los textos
figura.tight_layout()

# Guardamos el grafico como imagen en la carpeta de trabajo
figura.savefig("tarea_1_9_grafico.png", dpi=300)
print("""
La precision de 4 mm corresponde a una incertidumbre de ±0.4 cm.
      
El primer conjunto sigue casi perfectamente una parabola, con variaciones
mucho menores que la incertidumbre experimental, lo que sugiere datos
calculados o alterados y explica la nota 1.0.
      
En cambio, el segundo conjunto presenta variaciones compatibles con la
incertidumbre del instrumento, por lo que representa mejor datos experimentales reales.
""")

# Mostramos la ventana con los dos graficos
mlt.show()


