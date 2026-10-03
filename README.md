# TP Sistemas Inteligentes — Grupo 08 (UTN FRBA, 2C 2026)

Clasificación de 5 variedades de arroz (Arborio, Basmati, Ipsala, Jasmine y Karacadag) a partir de
imágenes, con redes neuronales convolucionales (Keras).

## Contenido

| Archivo | Descripción |
|---|---|
| `TP_Grupo08_Arroz_CNN.ipynb` | Notebook con todo el proceso (pensado para Google Colab) |
| `dividir_datos.py` | Script usado para dividir la muestra en entrenamiento y prueba |
| `data/train/` | Imágenes de entrenamiento (8.000 JPG, 1.600 por variedad) |
| `data/test/` | Imágenes de prueba (2.000 JPG, 400 por variedad) |
| `resultados/` | Gráficos, matrices de confusión y métricas (`resultados_cnn.json`) obtenidos en Colab |

## Cómo ejecutarlo

1. Abrir el notebook en Google Colab y elegir un entorno con GPU.
2. Ejecutar todas las celdas. Si la carpeta `data` no está, la primera celda pide el zip del repositorio.
3. Al terminar se generan los gráficos y las métricas en la carpeta `resultados/` (y se descarga `resultados_cnn.zip`).

## Modelos y resultados

| Modelo | Estructura | Pesos | Exactitud en prueba |
|---|---|---|---|
| Modelo 1 | Convolución (8) → agrupamiento → salida (5) | 38.669 | 98,55 % |
| Modelo 2 | Convolución (16) → agrupamiento → convolución (32) → agrupamiento → densa (64) → salida (5) | 406.885 | 97,70 % |
| Modelo 3 | Convolución (16) → agrupamiento → convolución (32) → agrupamiento → convolución (64) → agrupamiento → densa (64) → salida (5) | 171.429 | 98,85 % |

Los gráficos de error, las matrices de confusión y las métricas completas están en `resultados/`.

## Datos

Muestra de 10.000 imágenes (2.000 por variedad) del *Rice Image Dataset*:
Koklu, M., Cinar, I., Taspinar, Y.S. (2021). *Classification of rice varieties with deep learning methods*.
Computers and Electronics in Agriculture, 187, 106285.
https://www.kaggle.com/datasets/muratkokludataset/rice-image-dataset
