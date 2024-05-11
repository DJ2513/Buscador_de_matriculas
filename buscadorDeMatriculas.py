from datetime import date
from pathlib import Path
import os
import math
import time
import re

ruta = 'YOUR ROUTE'
hoy = date.today().strftime("%d/%m/%y")
patron = r'N\D{3}-\d{5}'
matriculas_encontradas = []
archivos = []

inicio = time.time()
def buscar_archivo(archivo, patron):
    openFile = open(archivo, 'r')
    texto = openFile.read()
    busqueda = re.search(patron, texto)
    if busqueda:
        return busqueda.group()
    else:
        return ''

def crear_listas():
    for root, dirs, files in os.walk(ruta):
        for file in files:
            archivo = Path(root, file)
            res = buscar_archivo(archivo, patron)
            if res != '':
                matriculas_encontradas.append(res)
                archivos.append(file.title())

def imprimir_busqueda():
    print('----------------------------------------------------')
    print(f'Fecha de busqueda: {hoy}')
    print("ARCHIVO \t\t\tNRO. SERIE")
    print("-------------- \t\t-----------")
    i = 0
    for m in matriculas_encontradas:
        print(archivos[i] + " \t\t" + m)
        i += 1
    print(f'Números encontrados: {len(matriculas_encontradas)}')
    fin = time.time()
    duracion = math.ceil(fin-inicio)
    print(f'Duración de la búsqueda: {duracion} segundos')
    print('----------------------------------------------------\n')


crear_listas()
imprimir_busqueda()
