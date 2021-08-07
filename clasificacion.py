import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns             #Para la visualización de datos basado en matplotlib
#Se importan las bibliotecas
import importlib
#Se importan las librerias necesarias para la regresión logística
from sklearn import linear_model
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from PIL import Image
import urllib.request


def clasificacion():
    
    st.title("Clasificación: Regresión Logística")
    BCancer = pd.read_csv('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/main/WDBCOriginal.csv')
    st.dataframe(BCancer)

    st.write("Observamos la distribución de los datos para la variable Diagnosis")
    st.text(BCancer.groupby("Diagnosis").size())

    #sns.pairplot(BCancer, hue="Diagnosis")
    #st.pyplot()
    importlib.reload(plt)

    st.write("Graficamos esta variable vs todas las demas variables")
    urllib.request.urlretrieve('https://raw.githubusercontent.com/danbruher/Proyecto-Mineria/6b5cd6687024d619184eb5478c9d9be6f2e38113/%C3%ADndice.png', "pairplot")
    image = Image.open('pairplot')
    st.image(image, caption='Relacion entre múltiples variables')

    st.header('''**Selección de características**''')

    st.subheader('''Matriz de correlaciones''')

    CorrBCancer = BCancer.corr(method="pearson")
    st.write(CorrBCancer)

    plt.figure(figsize=(14,7))
    MatrizInf = np.triu(CorrBCancer)
    sns.heatmap(CorrBCancer, cmap="RdBu_r", annot=True, mask=MatrizInf)
    st.pyplot()

    st.subheader('''Se seleccionan las variables predictoras (X) y la variable a pronosticar (Y)''')

    BCancer = BCancer.replace({"M":0, "B":1})
    st.write(BCancer)

    #Variables predictorias
    X = np.array(BCancer[["Texture","Area","Smoothness","Compactness","Symmetry","FractalDimension"]])
    #X = BCancer.iloc[:,[3,5,7,10,11]].values #.iloc para seleccionar filas y columnas según su posición
    pd.DataFrame(X)

    #Variable clase
    Y = np.array(BCancer[["Diagnosis"]])
    pd.DataFrame(Y)

    st.header("Aplicación del algoritmo")
    #Se declara el metodo de regresión logistica
    Clasificacion = linear_model.LogisticRegression()

    seed =1234
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=0.2, random_state=seed, shuffle = True)

    pd.DataFrame(X_train)

    pd.DataFrame(Y_train)

    Clasificacion.fit(X_train, Y_train)

    #Predicciones probabilísticas
    Probabilidad = Clasificacion.predict_proba(X_train)
    pd.DataFrame(Probabilidad)

    st.subheader("Predicciones con clasificación final")
    #Predicciones con clasificación final
    Predicciones = Clasificacion.predict(X_train)
    st.write(pd.DataFrame(Predicciones))

    st.subheader("Exactitud")
    #Para la evaluación de la exactitud (accuracy) se puede usar la función score()
    st.write(Clasificacion.score(X_train, Y_train))

    st.subheader("Validación del modelo")
    #Matriz de validación
    st.write("Matriz de validación")
    PrediccionesNuevas = Clasificacion.predict(X_validation)
    confusion_matrix = pd.crosstab(Y_validation.ravel(), PrediccionesNuevas, rownames=["real"], colnames=["Clasificación"])
    st.write(confusion_matrix)

    #Reporte de la clasificación
    st.write("Reporte de la clasificación")
    #st.write("Exactitud", Clasificacion.score(X_validation, Y_validation))
    st.text(classification_report(Y_validation, PrediccionesNuevas))

    st.subheader("Modelo de clasificación")
    #Ecuacion de modelo
    st.write(("Intercept: "))
    st.text(Clasificacion.intercept_)
    st.write("Coeficientes: \n")
    st.text(Clasificacion.coef_)

    st.header('''Sistema de inferencia basado en el modelo de regresión logística''')


    #Paciente P-92751 (569) -Tumor Benigno-
    
    
    with st.form("my_form"):
      st.header("Evaluar Paciente :hospital:")
      texture = st.number_input('Texture', format="%f")
      area = st.number_input('Area', format="%f")
      smoothness = st.number_input('Smoothness', format="%f")
      compactness = st.number_input('Compactness', format="%f")
      symmetry = st.number_input('Symmetry', format="%f")
      fractalDimension = st.number_input('FractalDimension', format="%f")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Evaluar")
      if submitted:
          NuevoPaciente1 = pd.DataFrame({'Texture': [texture], 'Area': [area], 'Smoothness': [smoothness], 'Compactness': [compactness], 'Symmetry': [symmetry], 'FractalDimension': [fractalDimension]})
          Evaluar=Clasificacion.predict(NuevoPaciente1)
          if(Evaluar==1):
            st.success("El paciente tiene un tumor benigno con un 88% de probabilidad. :white_check_mark:")
          elif (Evaluar==0):
            st.error("El paciente tiene un tumor maligno con un 88% de probabilidad. :bangbang:")