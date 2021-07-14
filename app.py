import streamlit as st
import numpy as np
import pandas as pd
import io
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('El proyecto de mineria')

uploaded_file = st.file_uploader("Subir archivo CSV")
DatosMelbourne = pd.read_csv(uploaded_file)
DatosMelbourne


st.subheader('Paso 1: Descripcion de la estructura de loas datos')
DatosMelbourne.shape
DatosMelbourne.dtypes

st.subheader('Paso 2: Indentificaion de datos faltantes.')
st.dataframe (DatosMelbourne.isnull().sum())


buffer = io.StringIO() 
DatosMelbourne.info(verbose=False, buf=buffer)
s = buffer.getvalue()
st.write (s)

st.subheader('Paso 3: Deteccion de valores atipicos')
a = DatosMelbourne.hist(figsize=(15,15))
st.pyplot()

st.dataframe(DatosMelbourne.describe())

st.subheader('Paso 4: Identificacion de relaciones entre varialbles')
ValoresAtipicos = ['Price', 'Landsize', 'BuildingArea','YearBuilt']
for col in ValoresAtipicos:
  sns.boxplot(col, data=DatosMelbourne)
  st.pyplot()

st.dataframe(DatosMelbourne.describe(include='object'))

for col in DatosMelbourne.select_dtypes(include='object'):
  if DatosMelbourne[col].nunique() < 10:sns.countplot(y = col, data=DatosMelbourne)
  st.pyplot()

for col in DatosMelbourne.select_dtypes(include='object'):
  if DatosMelbourne[col].nunique() < 10:
    st.dataframe(DatosMelbourne.groupby(col).agg(['mean']))

st.dataframe(DatosMelbourne.corr())