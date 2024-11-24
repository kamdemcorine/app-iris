#pip install plotly --upgrade
import streamlit as st
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt

#importation du jeu de donnees
data = pd.read_csv('auto-mpg.csv', delimiter = ',')

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
cols = st.columns((4.5, 4.5), gap = 'medium')
with cols[0]:
  # Créer un chart Altair pour afficher l'effectif de chaque modalite
  alt.Chart(data).mark_circle(size=60).encode( 
    x='horsepower:Q', 
    y='mpg:Q', 
    color='origin:N', 
    tooltip=['car name','mpg', 'horsepower'] ).properties(
    title='Relation entre Puissance et Consommation de Carburant' )
# Afficher le chart sur Streamlit 
  st.altair_chart(chart, use_container_width=True)

alt.Chart(data).mark_bar().encode( 
  x=alt.X('mpg:Q', bin=True), 
  y='count()', color='origin:N' ).properties( 
  title='Distribution de la Consommation de Carburant' )
st.altair_chart(chart, use_container_width = True)

with cols[1]:
  alt.Chart(data).mark_boxplot().encode( 
    x='model year:O', y='mpg:Q' ).properties( 
    title='Comparaison de la Consommation de Carburant par Année de Modèle' )
  st.altair_chart(chart, use_width_container = True)

alt.Chart(data).mark_bar().encode( 
  x='origin:N', y='count()', color='cylinders:O' ).properties( 
  title='Répartition des Voitures par Cylindres et Origine' )
st.altair_chart(chart, use_container_width = True)

alt.Chart(data).mark_line().encode(
    x='model year:O',
    y='mean(mpg):Q',
    color='origin:N'
).properties(
    title='Tendances de la Consommation de Carburant au Fil des Années')
st.altair_chart(chart, use_container_width = True)

with cols[2]:
  correlation_matrix = data.corr().reset_index().melt('index')
alt.Chart(correlation_matrix).mark_rect().encode(
    x='variable:N',
    y='index:N',
    color='value:Q').properties(
    title='Carte de Chaleur des Corrélations')

