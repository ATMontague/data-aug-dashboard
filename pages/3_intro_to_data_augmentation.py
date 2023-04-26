import streamlit as st
from streamlit_embedcode import github_gist


st.title('Introduction to Data Augmentation')

github_gist("https://gist.github.com/ATMontague/a5824b6d2a1c54d6eeaa65e50878a8a0")

url = "https://colab.research.google.com/gist/ATMontague/a5824b6d2a1c54d6eeaa65e50878a8a0/intro_to_data_augmentation.ipynb"

st.write("Click here to open and edit the notebook in Google Colab[link](%s)" % url)




