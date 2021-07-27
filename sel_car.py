import streamlit as st
import numpy as np
import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt


def sel_car(Datos):
    st.title('Seleccion de caracteristicas')
    st.write(Datos)



    st.subheader('Tipos de datos')
    st.dataframe(Datos.dtypes)


    st.subheader('Identificación de datos faltantes')
    st.dataframe(Datos.isnull().sum())

    st.subheader('Evalucaion visual')
    #sns.pairplot(Datos)
    #st.pyplot()

    fig, ax = plt.subplots()
    plt.plot(Datos['Rooms'], Datos['Bedroom2'], 'b+')
    plt.title('Gráfico de dispersión')
    plt.xlabel('Rooms')
    plt.ylabel('Bedroom2')
    st.pyplot()


    sns.scatterplot(x='Rooms', y ='Bedroom2', data=Datos, hue='Type')
    plt.title('Gráfico de dispersión')
    plt.xlabel('Rooms')
    plt.ylabel('Bedroom2')
    st.pyplot()


    plt.plot(Datos['YearBuilt'], Datos['Price'], 'b+')
    plt.title('Gráfico de dispersión')
    plt.xlabel('YearBuilt')
    plt.ylabel('Price')
    st.pyplot()

    sns.scatterplot(x='YearBuilt', y ='Price', data=Datos, hue='Type')
    plt.title('Gráfico de dispersión')
    plt.xlabel('YearBuilt')
    plt.ylabel('Price')
    st.pyplot()


    st.subheader('Identificación de relaciones entre variables')
    Datos.corr()

    plt.figure(figsize=(14,7))
    sns.heatmap(Datos.corr(), cmap='RdBu_r', annot=True)
    st.pyplot()

    plt.figure(figsize=(14,7))
    MatrizInf = np.triu(Datos.corr())
    sns.heatmap(Datos.corr(), cmap='RdBu_r', annot=True, mask=MatrizInf)
    st.pyplot()

    plt.figure(figsize=(14,7))
    MatrizSup = np.tril(Datos.corr())
    sns.heatmap(Datos.corr(), cmap='RdBu_r', annot=True, mask=MatrizSup)
    st.pyplot()

    Correlaciones = Datos.corr(method='pearson')
    st.write(Correlaciones)

    print(Correlaciones['Rooms'].sort_values(ascending=False)[:10], '\n')   #Top 10 valores


    st.subheader('Elección de variables')
    Datos.drop(['Bedroom2', 'Postcode', 'Lattitude', 'Longtitude'], axis=1)
    st.write(Datos)
    return Datos