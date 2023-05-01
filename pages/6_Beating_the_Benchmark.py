import streamlit as st
from streamlit_embedcode import github_gist


# todo: finish the notebook and then add it here

st.title('Beating the Benchmark')

github_gist("https://gist.github.com/ATMontague/4aad585d943ea074e4d575946901e87c")

url = "https://drive.google.com/file/d/1NNNn0qGm0AhG1qzW8pkyb-a_7tVXYXA3/view?usp=sharing"
st.write("Click here to open and edit the notebook in [Google Colab](%s)" % url)
