import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Iris.csv', delimiter = ';')
st.title('Mon premier dashboard avec Streamlit')
#st.table(data)

st.map(data)
