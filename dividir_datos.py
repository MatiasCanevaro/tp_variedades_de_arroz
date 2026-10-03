# Divide la muestra de 10.000 imagenes (2.000 por variedad) en
# entrenamiento (80 %) y prueba (20 %), manteniendo la proporcion de cada variedad.
import os
import random
import shutil

CLASES = ["Arborio", "Basmati", "Ipsala", "Jasmine", "Karacadag"]
ORIGEN = "rice-dataset"   # carpeta con una subcarpeta por variedad
random.seed(42)

for clase in CLASES:
    archivos = sorted(os.listdir(f"{ORIGEN}/{clase}"))
    random.shuffle(archivos)
    n_prueba = len(archivos) // 5          # 20 % para prueba
    for i, archivo in enumerate(archivos):
        destino = "test" if i < n_prueba else "train"
        os.makedirs(f"data/{destino}/{clase}", exist_ok=True)
        shutil.copy(f"{ORIGEN}/{clase}/{archivo}", f"data/{destino}/{clase}/{archivo}")
    print(clase, "->", len(archivos) - n_prueba, "entrenamiento,", n_prueba, "prueba")
