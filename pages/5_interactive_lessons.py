import streamlit as st
import streamlit.components.v1 as components

st.title("Jupyterlite in Streamlit")
components.iframe(
    'https://atmontague.github.io/edtech_notebooks/lab/index.html',
    height=500
)

# for optional opening in google colab
url = "https://colab.research.google.com/drive/1TWvtQhWS4lbxgMh-MOAvy2GscZLoTAeY#scrollTo=85_D2wb_HArq"
st.write("Click here to open the notebook in Google Colab [link](%s)" % url)