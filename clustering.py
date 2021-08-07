import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns             #Para la visualización de datos basado en matplotlib
#Se importan las bibliotecas
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import importlib
from kneed import KneeLocator


def clustering(data):
    st.title('Clustering')

    st.dataframe(data)
    columns_names = data.columns.values
    columns_names_list = list(columns_names)
    #'comprar' representa un valor obtenido de un análisis hipotecario preliminar
    genre = st.selectbox("What's your favorite movie genre",columns_names_list)
    st.text(data.groupby(genre).size())


    st.subheader('''Selección de características''')

   # sns.pairplot(data, hue='comprar')
   # st.pyplot()
   # plt.style.use('default')
    #importlib.reload(plt)

    CorrHipoteca = data.corr(method='pearson')

    plt.figure(figsize=(14,7))
    MatrizInf = np.triu(CorrHipoteca)
    sns.heatmap(CorrHipoteca, cmap='RdBu_r', annot=True, mask=MatrizInf)
    st.pyplot()

    st.subheader('''Selección de variables''')

    
    Valores= st.multiselect("Variables a agregar del dataset:", columns_names_list, default=columns_names_list)

    MHipoteca = np.array(data[Valores])
    pd.DataFrame(MHipoteca)
    st.write(MHipoteca)
  

    st.subheader('''Clustering particional Algoritmo: k-means''')
    

    #Definición de k clusters para K-means
    #Se utiliza random_state para inicializar el generador interno de números aleatorios
    try:
        SSE = []
        for i in range(2, 12):
            km = KMeans(n_clusters=i, random_state=0)
            km.fit(MHipoteca)
            SSE.append(km.inertia_)

        kl = KneeLocator(range(2, 12), SSE, curve="convex", direction="decreasing")
        kl.elbow

        plt.style.use('ggplot')
        kl.plot_knee()
        st.pyplot()

        numero = st.slider('Número de clusters', 2, 8)
        MParticional = KMeans(n_clusters=numero, random_state=0).fit(MHipoteca)
        MParticional.predict(MHipoteca)
        MParticional.labels_

        data['clusterP'] = MParticional.labels_
        

        st.write(data.groupby(['clusterP'])['clusterP'].count())

        plt.figure(figsize=(10, 7))
        plt.scatter(MHipoteca[:,0], MHipoteca[:,1], c=MParticional.labels_, cmap='rainbow')
        st.pyplot()

        CentroidesP = MParticional.cluster_centers_
        st.dataframe(pd.DataFrame(CentroidesP.round(numero), columns=Valores))

        # Gráfica de los elementos y los centros de los clusters
        from mpl_toolkits.mplot3d import Axes3D
        plt.rcParams['figure.figsize'] = (10, 7)
        plt.style.use('ggplot')
        colores=['red', 'blue', 'green', 'yellow','pink', 'orange', 'indigo', 'slategrey']
        asignar=[]
        for row in MParticional.labels_:
            asignar.append(colores[row])

        fig = plt.figure()
        ax = Axes3D(fig)
        ax.scatter(MHipoteca[:, 0], MHipoteca[:, 1], MHipoteca[:, 2], marker='o', c=asignar, s=60)
        ax.scatter(CentroidesP[:, 0], CentroidesP[:, 1], CentroidesP[:, 2], marker='*', c=colores[0:numero],s=1000)
        st.pyplot(fig)

        st.write('Casos representativos')
        Cercanos,_ = pairwise_distances_argmin_min(MParticional.cluster_centers_, MHipoteca)
        st.write(Cercanos)

        st.dataframe(data)
    except : 
        st.warning(":warning: Elimine datos categoricos del dataset para continuar")
    
   