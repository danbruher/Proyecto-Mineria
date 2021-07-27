import streamlit as st
import numpy as np
import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt
import home, eda, sel_car, pca, metricas,clustering, reglas

st.set_option('deprecation.showPyplotGlobalUse', False)

option=st.sidebar.selectbox('Selecciona Datos',('Hipoteca', 'Melbourne', 'Subir archivo csv'))
if option == 'Melbourne':
  Datos = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/melb_data.csv')
elif option == 'Hipoteca':
  Datos = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/Hipoteca.csv')
else:
  uploaded_file = st.sidebar.file_uploader("Subir archivo CSV", type =['.csv'])
  Datos = pd.read_csv(uploaded_file)

st.sidebar.title('Secciones')
options = st.sidebar.radio('', 
    ['Inicio', 'EDA', 'PCA'])

if options == 'Inicio':
    home.home()
elif options == 'EDA':
    eda.eda(Datos)
elif options == '2 Selección de características':
    sel_car.sel_car(Datos)
elif options == 'PCA':
    pca.pca(Datos)
elif options == 'Métricas Similitud':
    metricas.metricas(Datos)
elif options == 'Clustering':
    clustering.clustering(Datos)
elif options == 'Reglas Asociación':
    reglas.reglas(Datos)

#st.set_page_config(layout="centered")


