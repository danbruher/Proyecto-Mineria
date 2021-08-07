import streamlit as st
import numpy as np
import pandas as pd
import io
import seaborn as sns
import matplotlib.pyplot as plt
import home, eda, pca, clustering, clasificacion

st.set_option('deprecation.showPyplotGlobalUse', False)

def main():

    st.sidebar.header('Selecciona Datos :open_file_folder:')
    option=st.sidebar.selectbox('',('Melbourne', 'Hipoteca', 'Cancer','Subir archivo csv'))
    if option == 'Melbourne':
        Datos = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/melb_data.csv')
    elif option == 'Hipoteca':
        Datos = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/Hipoteca.csv')
    elif option == 'Cancer':
        Datos = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/WDBCOriginal.csv')
    else:
        uploaded_file = st.sidebar.file_uploader("Subir archivo CSV", type =['.csv'])
        try:
            Datos = pd.read_csv(uploaded_file)
        except ValueError:
             st.sidebar.error("Suba archivo csv")

    st.sidebar.write("\n \n")
    st.sidebar.header('Secciones :bookmark_tabs:')
    options = st.sidebar.radio('', 
        ['Inicio', 'EDA', 'PCA', 'Clustering', 'Clasificación'])

    if options == 'Inicio':
        home.home()
    elif options == 'EDA':
        eda.eda(Datos)
    elif options == 'PCA':
        pca.pca(Datos)
    elif options == 'Clustering':
        clustering.clustering(Datos)
    elif options == 'Clasificación':
        clasificacion.clasificacion()
        st.sidebar.info("Para clasificación se utlizará el dataset Cancer :grey_exclamation:")

#st.set_page_config(layout="centered")


if __name__ == '__main__':
	main()