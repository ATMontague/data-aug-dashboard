import streamlit as st
from streamlit_embedcode import github_gist


def main():

    st.title('Introduction to Data Augmentation')
    github_gist("https://gist.github.com/ATMontague/6ebb2d7edc7a354f1dc386c11cf6a399")
    url = "https://drive.google.com/file/d/108F60nYZ90LrZEJC5a3SnOHBciCBJsgE/view?usp=sharing"
    st.write("Click here to open and edit the notebook in [Google Colab](%s)" % url)


if __name__ == '__main__':
    main()

