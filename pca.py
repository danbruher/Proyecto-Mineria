import streamlit as st
import pandas as pd                                   # Para la manipulación y análisis de datos
import numpy as np                                    # Para crear vectores y matrices n dimensionales
import matplotlib.pyplot as plt                       # Para la generación de gráficas a partir de los datos
import seaborn as sns                                 # Para la visualización de datos basado en matplotlib              
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def pca(data):
    
    st.title('Ana;isis de componentes principales')
    st.write(data)

    st.subheader('Paso 1: Se hace una estandarización de los datos')
    normalizar = StandardScaler()                       # Se instancia el objeto StandardScaler 
    MHipoteca = data.drop(['comprar'], axis=1)      # Se quita la variable dependiente "Y"
    normalizar.fit(MHipoteca)                           # Se calcula la media y desviación para cada dimensión
    MNormalizada = normalizar.transform(MHipoteca)      # Se normalizan los datos 
    st.text(MNormalizada.shape)

    st.dataframe(pd.DataFrame(MNormalizada, columns=MHipoteca.columns))

    st.subheader('Paso 2 y3 :Se calcula la matriz de covarianzas o correlaciones, y se calculan los     componentes (eigen-vectores) y la varianza (eigen-valores)')
    Componentes = PCA(n_components=9)              # Se instancia el objeto PCA                          pca=PCA(n_components=None), pca=PCA(.85)
    Componentes.fit(MNormalizada)                  # Se obtiene los componentes
    X_Comp = Componentes.transform(MNormalizada)   # Se convierte los datos con las nuevas dimensiones
    #(pd.DataFrame(X_Comp)

    st.write(Componentes.components_)


    st.subheader('''Paso 4: Se decide el número de componentes principales
    * Se calcula el porcentaje de relevancia, es decir, entre el 75 y 90% de varianza total.
    * Se identifica mediante una gráfica el grupo de componentes con mayor varianza.
    * *Se elige las dimensiones cuya varianza sea mayor a 1.''')
    Varianza = Componentes.explained_variance_ratio_
    st.text('Eigenvalues:')
    st.text(Varianza)
    st.write('Varianza acumulada:', sum(Varianza[0:5]))   
    #Con 5 componentes se tiene el 85% de varianza acumulada y con 6 el 91%


    # Se grafica la varianza acumulada en las nuevas dimensiones
    plt.plot(np.cumsum(Componentes.explained_variance_ratio_))
    plt.xlabel('Número de componentes')
    plt.ylabel('Varianza acumulada')
    plt.grid()
    st.pyplot()

    st.subheader('''Paso 5: Se examina la proporción de relevancias –cargas–
    La importancia de cada variable se refleja en la magnitud de los valores en los 
    componentes (mayor magnitud es sinónimo de mayor importancia).Se revisan los 
    valores absolutos de los componentes principales seleccionados. Cuanto mayor sea el 
    valor absoluto, más importante es esa variable en el componente principal.''')
    st.write(pd.DataFrame(abs(Componentes.components_)))


    CargasComponentes = pd.DataFrame(Componentes.components_, columns=MHipoteca.columns)
    st.write(CargasComponentes)


    CargasComponentes = pd.DataFrame(abs(Componentes.components_), columns=MHipoteca.columns)
    st.write(CargasComponentes)

    columns_names = MHipoteca.columns.values
    columns_names_list = list(columns_names)
    Valores_a_drop= st.multiselect("Variables a dropear:", columns_names_list)

    NuevaMatriz = MHipoteca.drop(Valores_a_drop, axis=1)
    st.dataframe(NuevaMatriz)
    return NuevaMatriz