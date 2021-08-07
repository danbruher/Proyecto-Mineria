import streamlit as st

def home():
 
    st.title('GUI Minería de Datos :bar_chart:')
    st.write('### Creado por Daniel Brugada')
    st.write('''Herramienta desarrollada en lenguaje Python y el framework Streamlit para visualizar y modificar datasets
    en formato csv.''')
    st.write('''Para utilizar la aplicacion, suba su archivo en la barra lateral o utilice alguno de 
    los archivos incluidos, puede navegar en las distintas secciones con el 
    menú de navegación.''')
    st.write('\n')
    st.write('## Secciones')
    st.write('''**EDA:** Permite tener una idea de la estructura del conjunto de datos, identificar 
    la variable objetivo y posibles técnicas de modelado.''')
    st.write('''**PCA:** Para reducir la cantidad de variables de conjuntos de datos, mientras se 
    conserva la mayor cantidad de información posible.''')
    st.write('''**Clustering:** El objetivo es dividir una población heterogénea de elementos en un 
    número de grupos naturales, de acuerdo a sus similitudes.''')
    st.write('''**Clasificación:** Utiliza regresión logística para predecir valores binarios.''')
    st.write('## Código fuente y App')
    githublink = """<a href='https://github.com/danbruher/Proyecto-Mineria' target="_blank">https://github.com/danbruher/Proyecto-Mineria</a>"""
    st.write(f'\n\nRepositorio del proyecto: {githublink}. ', unsafe_allow_html=True)
    applink = """<a href='https://mineria-de-datos.herokuapp.com/' target="_blank">https://mineria-de-datos.herokuapp.com/</a>"""
    st.write(f'\n\nApp: {applink}. ', unsafe_allow_html=True)