#pip install plotly --upgrade

import streamlit as st
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt

#importation du jeu de donnees
data = pd.read_csv('Iris.csv', delimiter = ';')

#titre du tableau de bord
st.title('Visualisation du jeu de donnees')

#onglets du tableau de bord
#titres_onglets = ['visualisation','modele de machine learning', 'evaluation du modele']
#onglets = st.tabs(titres_onglets)


#creation d'un sidebar
with st.sidebar:
  st.title('parametres du dashboard')
  st.selectbox("selectionner une classe:", ["Setosa","Versicolor","Virginica"])
  st.header('Selection de couleur')
  speciesSlide = st.slider("Data:", "setosa", "versicolor", "virginica")
  st.write("espece:", slide_espece)


# Créer un chart Altair pour afficher l'effectif de chaque modalite
species_values = data['Species'].value_counts().reset_index()
species_values.columns = ['Species','count']
chart = alt.Chart(species_values).mark_bar().encode(
  x='Species', 
  y='count').properties(
  title = 'Effectif de chaque modalite du jeu de donnees Iris')
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalLength') 
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalWidth') 
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)


chart = alt.Chart(data).mark_point().encode( x='SepalWidth', y='PetalLength') 
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)


chart = alt.Chart(data).mark_point().encode( x='Petalwidth', y='PetalLength') 
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)



lines = (
    alt.Chart(data, title="Evolution of stock prices")
    .mark_line()
    .encode(
        x="SepalLength",
        y="Species",
        color="symbol",
    )
)
