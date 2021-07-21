import streamlit as st
import pandas as pd                                   # Para la manipulación y análisis de datos
import numpy as np                                    # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt                       # Para la generación de gráficas a partir de los datos
import seaborn as sns                                 # Para la visualización de datos basado en matplotlib              
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def pca(data):
    
    st.write(data)

    normalizar = StandardScaler()                       # Se instancia el objeto StandardScaler 
    MHipoteca = data.drop(['comprar'], axis=1)      # Se quita la variable dependiente "Y"
    normalizar.fit(MHipoteca)                           # Se calcula la media y desviación para cada dimensión
    MNormalizada = normalizar.transform(MHipoteca)      # Se normalizan los datos 
    MNormalizada.shape

    pd.DataFrame(MNormalizada, columns=MHipoteca.columns)


    Componentes = PCA(n_components=9)              # Se instancia el objeto PCA                          pca=PCA(n_components=None), pca=PCA(.85)
    Componentes.fit(MNormalizada)                  # Se obtiene los componentes
    X_Comp = Componentes.transform(MNormalizada)   # Se convierte los datos con las nuevas dimensiones
    #pd.DataFrame(X_Comp)


    Varianza = Componentes.explained_variance_ratio_
    print('Eigenvalues:', Varianza)
    print('Varianza acumulada:', sum(Varianza[0:5]))   
    #Con 5 componentes se tiene el 85% de varianza acumulada y con 6 el 91%


    # Se grafica la varianza acumulada en las nuevas dimensiones
    plt.plot(np.cumsum(Componentes.explained_variance_ratio_))
    plt.xlabel('Número de componentes')
    plt.ylabel('Varianza acumulada')
    plt.grid()
    st.pyplot()


    print(pd.DataFrame(abs(Componentes.components_)))


    CargasComponentes = pd.DataFrame(Componentes.components_, columns=MHipoteca.columns)
    CargasComponentes


    CargasComponentes = pd.DataFrame(abs(Componentes.components_), columns=MHipoteca.columns)
    CargasComponentes

    NuevaMatriz = MHipoteca.drop(['ahorros', 'vivienda', 'estado_civil', 'hijos'], axis=1)
    NuevaMatriz