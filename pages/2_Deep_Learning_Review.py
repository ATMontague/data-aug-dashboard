import streamlit as st
from streamlit_embedcode import github_gist


# todo: finish the notebook and then add it here

st.title('A Brief Review of Deep Learning')

github_gist("https://gist.github.com/ATMontague/4af8d99f801f8af74efe434aacde72e1")

url = "https://drive.google.com/file/d/1EQUan6Q3kXlpTge1b2y2gBs4E-ffvtbG/view?usp=sharing"
st.write("Click here to open and edit the notebook in [Google Colab](%s)" % url)
