"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""

import pandas as pd

# Variable global para almacenar el DataFrame
dataframe = None

def ingest_data():
    global dataframe
    
    # Si no, procedemos a generar el DataFrame
    data = []

    with open("clusters_report.txt", "r") as file:
        for _ in range(3):
            next(file)

        for line in file:
            parts = line.split(maxsplit=3)
            if len(parts) < 4:
                continue
            try:
                cluster = int(parts[0])
                cantidad = int(parts[1])
                porcentaje = float(parts[2].replace(',', '.'))
            except ValueError:
                continue
            palabras_clave = parts[3].strip().replace('  ', '').replace('%', '')

            palabras_clave = palabras_clave.lstrip().rstrip()
            
            parts[3:3] = parts[2].strip().replace(',', '')
            data.append([cluster, cantidad, porcentaje, palabras_clave])

    dataframe = pd.DataFrame(data, columns=["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])
    dataframe.columns = dataframe.columns.str.lower().str.replace(' ', '_')

    return dataframe

ingest_data()

#print(dataframe)











