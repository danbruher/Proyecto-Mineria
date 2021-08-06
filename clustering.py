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
    #'comprar' representa un valor obtenido de un análisis hipotecario preliminar
    st.write(print(data.groupby('comprar').size()))


    st.subheader('''#### **Paso 1: Selección de características**
    Se utiliza una matriz de correlaciones con el propósito de definir un grupo de características significativas.''')

    sns.pairplot(data, hue='comprar')
    st.pyplot()
    plt.style.use('default')
    importlib.reload(plt)
    #importlib.reload(sns)

    #plt.plot(Hipoteca['ingresos'], Hipoteca['gastos_comunes'], 'b+')
    sns.scatterplot(x='ingresos', y ='gastos_comunes', data=data, hue='comprar', s=10)
    plt.title('Gráfico de dispersión')
    plt.xlabel('Ingresos')
    plt.ylabel('Gastos comunes')
    st.pyplot()


    #plt.plot(Hipoteca['ingresos'], Hipoteca['ahorros'], 'b+')
    sns.scatterplot(x='ingresos', y ='ahorros', data=data, hue='comprar')
    plt.title('Gráfico de dispersión')
    plt.xlabel('Ingresos')
    plt.ylabel('Ahorros')
    st.pyplot()

    CorrHipoteca = data.corr(method='pearson')
    st.dataframe(CorrHipoteca)

    plt.figure(figsize=(14,7))
    MatrizInf = np.triu(CorrHipoteca)
    sns.heatmap(CorrHipoteca, cmap='RdBu_r', annot=True, mask=MatrizInf)
    st.pyplot()

    print(CorrHipoteca['ingresos'].sort_values(ascending=False)[:10], '\n')   #Top 10 valores
    print(CorrHipoteca['trabajo'].sort_values(ascending=False)[:10], '\n')   #Top 10 valores

    st.subheader('''**Selección de variables:**
    a) A pesar de existir 2 correlaciones altas, entre 'ingresos' y 'ahorros' (0.71) y 'trabajo' e 'hijos' (0.69);  éstas se tomarán en cuenta para obtener una segmentación que combine las variables mediante la similitud de los elementos.

    b) Se suprimirá la variable 'comprar' debido a que representa inherentemente un agrupamiento, y fue un campo calculado con base a un análisis hipotecario preliminar.''')


    MHipoteca = np.array(data[['ingresos', 'gastos_comunes', 'pago_coche', 'gastos_otros', 'ahorros', 'vivienda', 'estado_civil', 'hijos', 'trabajo']])
    pd.DataFrame(MHipoteca)
    #MHipoteca = Hipoteca.drop(['comprar'], axis=1)
    #MHipoteca

    st.subheader('''I. Clustering particional 
    Algoritmo: k-means''')
    

    #Definición de k clusters para K-means
    #Se utiliza random_state para inicializar el generador interno de números aleatorios
    SSE = []
    for i in range(2, 12):
        km = KMeans(n_clusters=i, random_state=0)
        km.fit(MHipoteca)
        SSE.append(km.inertia_)

    #Se grafica SSE en función de k
    plt.figure(figsize=(10, 7))
    plt.plot(range(2, 12), SSE, marker='o')
    plt.xlabel('Cantidad de clusters *k*')
    plt.ylabel('SSE')
    plt.title('Elbow Method')
    st.pyplot()


    st.subheader('Observación. En la práctica, puede que no exista un codo afilado (codo agudo) y, como método heurístico, ese "codo" no siempre puede identificarse sin ambigüedades.')

    kl = KneeLocator(range(2, 12), SSE, curve="convex", direction="decreasing")
    kl.elbow

    plt.style.use('ggplot')
    kl.plot_knee()
    st.pyplot()

    MParticional = KMeans(n_clusters=4, random_state=0).fit(MHipoteca)
    MParticional.predict(MHipoteca)
    MParticional.labels_

    data['clusterP'] = MParticional.labels_
    st.dataframe(data)

    data.groupby(['clusterP'])['clusterP'].count()

    plt.figure(figsize=(10, 7))
    plt.scatter(MHipoteca[:,0], MHipoteca[:,1], c=MParticional.labels_, cmap='rainbow')
    st.pyplot()

    CentroidesP = MParticional.cluster_centers_
    pd.DataFrame(CentroidesP.round(4), columns=['ingresos','gastos_comunes','pago_coche','gastos_otros','ahorros','vivienda','estado_civil','hijos','trabajo'])

    # Gráfica de los elementos y los centros de los clusters
    from mpl_toolkits.mplot3d import Axes3D
    plt.rcParams['figure.figsize'] = (10, 7)
    plt.style.use('ggplot')
    colores=['red', 'blue', 'green', 'yellow']
    asignar=[]
    for row in MParticional.labels_:
        asignar.append(colores[row])

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(MHipoteca[:, 0], MHipoteca[:, 1], MHipoteca[:, 2], marker='o', c=asignar, s=60)
    ax.scatter(CentroidesP[:, 0], CentroidesP[:, 1], CentroidesP[:, 2], marker='*', c=colores, s=1000)
    st.pyplot(fig)

    #Se identifica las personas más cercanas al centroide (casos representativos)
    Cercanos,_ = pairwise_distances_argmin_min(MParticional.cluster_centers_, MHipoteca)
    Cercanos

    st.dataframe(data.head(10))

    Personas = data['ingresos'].values
    for row in Cercanos:
        print(Personas[row])

   