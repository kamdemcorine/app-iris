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

  # Widget pour sélectionner une couleur 
  color = st.color_picker('Choisissez une couleur', '#00f900') 
  st.write('La couleur sélectionnée est', color)

# Créer les colonnes 
col1, col2, col3, col4 = st.columns(4)
with col1:
  # Créer un chart Altair pour afficher l'effectif de chaque modalite
  species_values = data['Species'].value_counts().reset_index()
  species_values.columns = ['Species','count']
  chart = alt.Chart(species_values).mark_bar().encode(
    x='Species', 
    y='count',
    color = alt.value(color)).properties(
    title = 'Distribution des especes d\'iris')
  # Afficher le chart sur Streamlit 
  st.altair_chart(chart, use_container_width=True)

with col2:
  chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalLength') 
  # Afficher le chart sur Streamlit 
  st.altair_chart(chart, use_container_width=True)

with col3:
  chart = alt.Chart(data).mark_point().encode( 
    x='SepalWidth', y='PetalLength',
    color = alt.value(color)).properties(
    title = 'Correlation entre la longueur des sepales et des petales') 
  # Afficher le chart sur Streamlit 
  st.altair_chart(chart, use_container_width=True)
with col4:
  #Correlation entre la largeur des petales et des sepales
  chart = alt.Chart(data).mark_point().encode( 
    x='PetalWidth', y='PetalWidth',
    color = alt.value(color)).properties(
    title = 'Correlation entre la largeur des petales et des sepales')
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
