import streamlit as st
import numpy as np      # Para crear vectores y matrices n dimensionales
import pandas as pd     # Para la manipulación y análisis de datos
import io       
import seaborn as sns   # Para la visualización de datos basado en matplotlib
import matplotlib.pyplot as plt # Para la generación de gráficas a partir de los datos
import importlib


#st.set_page_config(layout="centered")

st.set_option('deprecation.showPyplotGlobalUse', False)


def eda(Datos):
    st.title('EDA')
    st.subheader('Descripcion de la estructura de los datos')
    st.dataframe(Datos)
    st.write('''Cantidad de filas y columnas que tiene el conjunto de datos.''')
    st.text(Datos.shape)

    st.write('''Tipos de datos de las columnas ''')
    st.text(Datos.dtypes)


    st.subheader('Identificación de datos faltantes.')
    st.write('''Suma de todos los valores nulos en cada variable.''')
    st.text (Datos.isnull().sum())

    st.write('''Tipo de datos y la suma de valores no nulos.''')
    buffer = io.StringIO() 
    Datos.info(buf=buffer)
    s = buffer.getvalue() 
    with open("df_info.txt", "w", encoding="utf-8") as f:
     st.text(s) 

    st.subheader('Deteccion de valores atipicos')
    st.write('''Se utilizan histogramas que agrupan los números en rangos. La altura de una barra 
    muestra cuántos números caen en ese rango.''')
    fig, ax = plt.subplots()
    Datos.hist(figsize=(15,15))
    st.pyplot()

    st.write('''Resumen estadístico de variables numéricas ''')
    st.write(Datos.describe())
    importlib.reload(plt)
    st.write('''Diagramas para detectar posibles valores atípicos.''')
    columns_names = Datos.columns.values
    columns_names_list = list(columns_names)
    ValoresAtipicos= st.multiselect("Variables atipicas:", columns_names_list)
    
    
    fig, ax = plt.subplots()
    for col in ValoresAtipicos:
        ax = sns.boxplot(col, data=Datos)
        st.pyplot()

    st.write('''Distribución de variables categóricas''')
    try:
        st.dataframe(Datos.describe(include='object'))
    except ValueError:
        st.error('Sin datos categóricos')

    for col in Datos.select_dtypes(include='object'):
        if Datos[col].nunique() < 10:
            fig, ax = plt.subplots()
            ax = sns.countplot(y = col, data=Datos)
            st.pyplot()

    for col in Datos.select_dtypes(include='object'):
     if Datos[col].nunique() < 10:
        st.dataframe(Datos.groupby(col).agg(['mean']))


    st.subheader('Identificacion de relaciones entre pares de varialbles')
    st.write('''Una matriz de correlaciones es útil para analizar la relación entre las variables 
    numéricas. ''')
    st.dataframe(Datos.corr())

    plt.figure(figsize=(14,14))
    sns.heatmap(Datos.corr(), cmap='RdBu_r', annot=True)
    st.pyplot()