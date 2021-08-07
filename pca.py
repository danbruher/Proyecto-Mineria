import streamlit as st
import pandas as pd                                   # Para la manipulación y análisis de datos
import numpy as np                                    # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt                       # Para la generación de gráficas a partir de los datos
import seaborn as sns                                 # Para la visualización de datos basado en matplotlib              
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def pca(data):
    
    st.title('Análisis de componentes principales')
    
    st.subheader('Estandarización de los datos')
    st.write(data)
    columns_namess = data.columns.values
    columns_names_listt = list(columns_namess)
    Valores_a_dropear= st.multiselect("Variables a dropear:", columns_names_listt)
    normalizar = StandardScaler()                       # Se instancia el objeto StandardScaler 
    MHipoteca = data.drop(Valores_a_dropear, axis=1)      # Se quita la variable dependiente "Y"
    try:
        normalizar.fit(MHipoteca)
        MNormalizada = normalizar.transform(MHipoteca)      # Se normalizan los datos 
        st.text(MNormalizada.shape)                        # Se calcula la media y desviación para cada dimensión
        
        st.dataframe(pd.DataFrame(MNormalizada, columns=MHipoteca.columns))

        st.write('Se calcula la matriz de covarianzas, y se calculan los componentes  y la varianza')
        Componentes = PCA(n_components=None)              # Se instancia el objeto PCA                          pca=PCA(n_components=None), pca=PCA(.85)
        Componentes.fit(MNormalizada)                  # Se obtiene los componentes
        X_Comp = Componentes.transform(MNormalizada)   # Se convierte los datos con las nuevas dimensiones
        #(pd.DataFrame(X_Comp)

        st.write(Componentes.components_)

        st.subheader('''Se decide el número de componentes principales''')
        numero = st.slider('Número de componetes', 0, 10)
        Varianza = Componentes.explained_variance_ratio_
        st.text('Eigenvalues:')
        st.text(Varianza)
        st.write('Varianza acumulada:', sum(Varianza[0:numero]))   
        
        # Se grafica la varianza acumulada en las nuevas dimensiones
        plt.plot(np.cumsum(Componentes.explained_variance_ratio_))
        plt.xlabel('Número de componentes')
        plt.ylabel('Varianza acumulada')
        plt.grid()
        st.pyplot()

        st.subheader('''Se examina la proporción de relevancias.''')
        pd.DataFrame(abs(Componentes.components_))

        CargasComponentes = pd.DataFrame(Componentes.components_, columns=MHipoteca.columns)
        CargasComponentes = pd.DataFrame(abs(Componentes.components_), columns=MHipoteca.columns)
        st.write(CargasComponentes)

        columns_names = MHipoteca.columns.values
        columns_names_list = list(columns_names)
        Valores_a_drop= st.multiselect("Variables a dropear del dataset:", columns_names_list)

        NuevaMatriz = MHipoteca.drop(Valores_a_drop, axis=1)
        st.dataframe(NuevaMatriz)
        return NuevaMatriz
    except:
        st.warning(" :warning: Elimine datos categoricos del dataset para continuar")