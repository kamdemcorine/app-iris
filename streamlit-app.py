import streamlit as st
import pandas as pd
import plotly.express as px
#import matplotlib.pyplot as plt


data = pd.read_csv('Iris.csv', delimiter = ';')
st.title('Mon premier dashboard avec Streamlit')
#st.table(data)
fig = px.box(data, x='SepalLength', y='Species')

st.plotly_chart(fig, use_container_width=True)
