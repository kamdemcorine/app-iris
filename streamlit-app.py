import streamlit as st
import pandas as pd

data = pd.read_csv('Iris.csv', delimiter = ';')
st.title('Mon premier dashboard avec Streamlit')
#st.table(data)

# Tab 2: Visualization
with tab2:
  st.header("Visualization")
  # Add your visualization code here (e.g., countplot, histogram)
  st.subheader("Distribution of Species")
  fig1 = plt.figure()
  sns.countplot(x="Species", data=df)
  plt.title('distribution des especes d\'iris')
  st.pyplot(fig1)
