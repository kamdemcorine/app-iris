#pip install plotly --upgrade

import streamlit as st
import pandas as pd
import altair as alt
#import matplotlib.pyplot as plt

#importation du jeu de donnees
data = pd.read_csv('Iris.csv', delimiter = ';')
#creation d'un sidebar
with st.sidebar:
#ajouter le titre
  st.title('Mon premier dashboard avec Streamlit')
#st.title('Mon premier dashboard avec Streamlit')
#st.table(data)

# Créer un chart Altair pour afficher l'effectif de chaque modalite
values = data['Species'].value_counts().reset_index()
species_count.columns = ['Species','count']
chart = alt.Chart(species_count).mark_bar().encode(
  x='Species', 
  y='count').properties(
  title = 'Effectif de chaque modalite du jeu de donnees Iris')
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)

chart = alt.Chart(data).mark_point().encode( x='SepalLength', y='PetalLength') 
# Afficher le chart sur Streamlit 
st.altair_chart(chart, use_container_width=True)

with st.sidebar:
  st.title('Iris visualisation menu')
  st.selectbox("selectionner une classe:", ["Setosa","Versicolor","Virginica"])

  speciesSlide = st.slider("Data", "setosa", "versicolor", "virginica")
  st.write("espece:", slide_espece)
  #speciesSlide = st.slider("Especes", 'Setosa','Versicolor','Virginica')

lines = (
    alt.Chart(data, title="Evolution of stock prices")
    .mark_line()
    .encode(
        x="SepalLength",
        y="Species",
        color="symbol",
    )
)
