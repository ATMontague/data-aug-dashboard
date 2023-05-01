import streamlit as st
from streamlit_embedcode import github_gist


# todo: finish the notebook and then add it here

st.title('Beating the Benchmark')

github_gist("https://gist.github.com/ATMontague/7177c0247cccbc48eed4a7729a45da81")

url = "https://drive.google.com/file/d/1NNNn0qGm0AhG1qzW8pkyb-a_7tVXYXA3/view?usp=sharing"
st.write("Click here to open and edit the notebook in [Google Colab](%s)" % url)
