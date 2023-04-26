import streamlit as st
from streamlit_embedcode import github_gist


st.title('Introduction to Classification')

github_gist("https://gist.github.com/ATMontague/924717107bb1111308733af2b7718f8b")

url = "https://colab.research.google.com/drive/1TWvtQhWS4lbxgMh-MOAvy2GscZLoTAeY#scrollTo=85_D2wb_HArq"
st.write("Click here to open and edit the notebook in Google Colab[link](%s)" % url)
