import streamlit as st
from streamlit_embedcode import github_gist


st.title('Introduction to Image Classification')

github_gist("https://gist.github.com/ATMontague/fe75ea58fb9e00dac488d355fec612d3")

url = "https://drive.google.com/file/d/1TnGRuYhBG8483KghYyXWQ0kwEQN4631w/view?usp=sharing"
st.write("Click here to open and edit the notebook in [Google Colab](%s)" % url)
