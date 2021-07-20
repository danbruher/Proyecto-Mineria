import streamlit as st
import numpy as np
import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt

st.sidebar.title('Opciones')
uploaded_file = st.sidebar.file_uploader("Subir archivo CSV", type =['.csv'])
option=st.sidebar.selectbox('Selecciona Datos',('Melbourne','Hipoteca', 'Archivo subido'))
if option == 'Melbourne':
  DatosMelbourne = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/melb_data.csv')
elif option == 'Hipoteca':
  DatosMelbourne = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/Hipoteca.csv')
else:
  DatosMelbourne = pd.read_csv(uploaded_file)

#st.set_page_config(layout="centered")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('El proyecto de mineria')



DatosMelbourne


st.subheader('Paso 1: Descripcion de la estructura de loas datos')
st.text(DatosMelbourne.shape)
st.dataframe(DatosMelbourne.dtypes)

st.subheader('Paso 2: Indentificaion de datos faltantes.')
st.dataframe (DatosMelbourne.isnull().sum())


buffer = io.StringIO() 
DatosMelbourne.info(verbose = True, buf=buffer)
s = buffer.getvalue()
st.write (s)


st.subheader('Paso 3: Deteccion de valores atipicos')

fig, ax = plt.subplots()
DatosMelbourne.hist(figsize=(15,15))
st.pyplot()

st.dataframe(DatosMelbourne.describe())

st.subheader('Paso 4: Identificacion de relaciones entre varialbles')
ValoresAtipicos = ['Price', 'Landsize', 'BuildingArea','YearBuilt']
fig, ax = plt.subplots()
for col in ValoresAtipicos:
  ax = sns.boxplot(col, data=DatosMelbourne)
  st.pyplot(fig)

st.dataframe(DatosMelbourne.describe(include='object'))

for col in DatosMelbourne.select_dtypes(include='object'):
  if DatosMelbourne[col].nunique() < 10:
    fig, ax = plt.subplots()
    ax = sns.countplot(y = col, data=DatosMelbourne)
    st.pyplot(fig)

for col in DatosMelbourne.select_dtypes(include='object'):
  if DatosMelbourne[col].nunique() < 10:
    st.dataframe(DatosMelbourne.groupby(col).agg(['mean']))

st.dataframe(DatosMelbourne.corr())

