"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
from datetime import datetime
import os

def pregunta_01():

    if not os.path.exists("files/output"):
        os.makedirs("files/output")
    

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";",header=0,index_col="Unnamed: 0")


    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    def convertir_fecha(fecha):
        formatos = ['%d/%m/%Y', '%Y/%m/%d']  # Lista de posibles formatos
        for formato in formatos:
            try:
                return datetime.strptime(fecha, formato).strftime('%Y-%m-%d')
            except ValueError:
                continue
        raise ValueError(f"No se pudo procesar la fecha: {fecha}")
    
    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(convertir_fecha)

    df["sexo"] = df['sexo'].str.lower()
    df["tipo_de_emprendimiento"] = df['tipo_de_emprendimiento'].str.lower()

    df["idea_negocio"] = df['idea_negocio'].str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace(" ", "_", regex=False)
    df["idea_negocio"] = df["idea_negocio"].str.replace("-", "_", regex=False)

    df["línea_credito"] = df['línea_credito'].str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace(" ", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace("-", "_", regex=False)
    df["línea_credito"] = df["línea_credito"].str.replace(".", "", regex=False)

    df["barrio"] = df["barrio"].str.lower()
    df["barrio"] = df["barrio"].str.replace("_", " ", regex=False)
    df["barrio"] = df["barrio"].str.replace("-", " ", regex=False)
    df["barrio"] = df["barrio"].str.replace(".", "", regex=False)

    df["monto_del_credito"] = df["monto_del_credito"].str.strip("$")
    df["monto_del_credito"] = df["monto_del_credito"].str.strip()
    df["monto_del_credito"] = df["monto_del_credito"].map(lambda x: x[:-3] if x[-3:] == ".00" else x)
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(",","")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".","")
    df["monto_del_credito"] = df["monto_del_credito"].map(lambda x: int(x))

    df.drop_duplicates(inplace=True)

    #Guardar el Dataframe en la carpeta files/output
    df.to_csv("files/output/solicitudes_de_credito.csv", encoding="utf-8",sep=";")

    return df


    # """
    # Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    # El archivo tiene problemas como registros duplicados y datos faltantes.
    # Tenga en cuenta todas las verificaciones discutidas en clase para
    # realizar la limpieza de los datos.

    # El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    # """
