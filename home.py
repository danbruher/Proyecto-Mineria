import streamlit as st

def home():
 
    st.title('GUI Minería de Datos')
    st.write('## Interface gráfica de usuario')
    st.write('### Creado por Daniel Brugada')
    st.write('''Herramietna desarrollada en Python y Streamlit para visulizar y modificar datasets
    en formato csv.''')
    st.write('''Para utilizar la aplicacion, suba su archivo en la barra lateral o utilice alguno de 
    los archivos incluidos . Una vez echo esto, puede navegar en las distitnas herramintas con el 
    menu de navegacion.''')
    st.write('\n')
    st.write('## Secciones')
    st.write('''**EDA:** Permite tener una idea de la estructura del conjunto de datos, identificar 
    la variable objetivo y posibles técnicas de modelado.''')
    st.write('''**PCA:** Para reducir la cantidad de variables de conjuntos de datos, mientras se 
    conserva la mayor cantidad de información posible.''')
    st.write('''**Metricas de similitud:** Es una puntuación objetiva que resume la diferencia entre 
    dos elementos.''')
    st.write('''**Clustering:** El objetivo es dividir una población heterogénea de elementos en un 
    número de grupos naturales (regiones o segmentos homogéneos), de acuerdo a sus similitudes.''')
    st.write('''**Reglas de asociacion:** Consiste en identificar un conjunto de patrones secuenciales 
    en forma de reglas de tipo: A => B''')
    st.write('## Codigo fuente, Documentacion')
    githublink = """<a href='https://github.com/danbruher/Proyecto-Mineria' target="_blank">https://github.com/danbruher/Proyecto-Mineria</a>"""
    st.write(f'\n\nRepositorio del proyecto: {githublink}. ', unsafe_allow_html=True)