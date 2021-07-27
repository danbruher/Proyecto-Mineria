import streamlit as st
import numpy as np      # Para crear vectores y matrices n dimensionales
import pandas as pd     # Para la manipulación y análisis de datos
import io       
import seaborn as sns   # Para la visualización de datos basado en matplotlib
import matplotlib.pyplot as plt # Para la generación de gráficas a partir de los datos


#st.set_page_config(layout="centered")

st.set_option('deprecation.showPyplotGlobalUse', False)


def eda(Datos):
    st.title('EDA')
    st.dataframe(Datos)


    st.subheader('Paso 1: Descripcion de la estructura de loas datos')
    st.write('''Forma (dimensiones) del DataFrame 
    El atributo .shape de Pandas proporciona una estructura general de los datos. 
    Devuelve la cantidad de filas y columnas que tiene el conjunto de datos.''')
    st.text(Datos.shape)

    st.write('''2) Tipos de datos (variables)El atributo .dtypes muestra los tipos 
    de datos de las columnas (variables y tipos)''')
    st.dataframe(Datos.dtypes)



    st.subheader('Paso 2: Indentificaion de datos faltantes.')
    st.write('''Una función útil de pandas es .isnull().sum() 
    que regresa la suma de todos los valores nulos en cada variable.)''')
    st.dataframe (Datos.isnull().sum())

    buffer = io.StringIO() 
    Datos.info(buf=buffer)
    s = buffer.getvalue() 
    with open("df_info.txt", "w", encoding="utf-8") as f:
     f.write(s) 

    st.subheader('Paso 3: Deteccion de valores atipicos')
    st.write('''Se utilizan histogramas que agrupan los números en rangos. La altura de una barra 
    muestra cuántos números caen en ese rango. Se emplea hist() para trazar el histograma de las 
    variables numéricas. ''')
    fig, ax = plt.subplots()
    Datos.hist(figsize=(15,15))
    st.pyplot()

    st.write('''Resumen estadístico de variables numéricas Se sacan estadísticas usando describe() 
    que muestra un resumen estadístico de las variables numéricas.''')
    st.dataframe(Datos.describe())

    st.write('''3) Diagramas para detectar posibles valores atípicos Para este tipo de gráficos 
    se utiliza Seaborn, que permite generar diagramas de cajas para detectar valores atípicos.''')
    columns_names = Datos.columns.values
    columns_names_list = list(columns_names)
    ValoresAtipicos= st.multiselect("Variables atipicas:", columns_names_list)
    #ValoresAtipicos = ['Price', 'Landsize', 'BuildingArea','YearBuilt']
    
    fig, ax = plt.subplots()
    for col in ValoresAtipicos:
        ax = sns.boxplot(col, data=Datos)
        st.pyplot()

    st.write('''4) Distribución de variables categóricas Se refiere a la observación de las clases 
    de cada columna (variable) y su frecuencia. Aquí, los gráficos ayudan para tener una idea 
    general de las distribuciones, mientras que las estadísticas dan números reales.''')
    try:
        st.dataframe(Datos.describe(include='object'))
    except ValueError:
        st.error('Sin datos categoricos')

    st.write('''Plot Para este tipo de gráficos se utiliza Seaborn, que permite generar un 
    histograma para variables categóricas. Cada barra en el gráfico de conteo representa una clase. 
    Se crea un bucle para el conteo y distribución de las clases. La sentencia select_dtypes(include 
    = ’object’) selecciona las columnas categóricas con sus valores y las muestra. Se incluye 
    también If para elegir solo las tres columnas con 10 o menos clases usando series.nunique() < 
    10.''')
    for col in Datos.select_dtypes(include='object'):
        if Datos[col].nunique() < 10:
            fig, ax = plt.subplots()
            ax = sns.countplot(y = col, data=Datos)
            st.pyplot()

    for col in Datos.select_dtypes(include='object'):
     if Datos[col].nunique() < 10:
        st.dataframe(Datos.groupby(col).agg(['mean']))


    st.subheader('Paso 4: Identificacion de relaciones entre pares de varialbles')
    st.write('''Una matriz de correlaciones es útil para analizar la relación entre las variables 
    numéricas. Se emplea la función corr()''')
    st.dataframe(Datos.corr())

    plt.figure(figsize=(14,14))
    sns.heatmap(Datos.corr(), cmap='RdBu_r', annot=True)
    st.pyplot()