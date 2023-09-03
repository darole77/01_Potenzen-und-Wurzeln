import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Rechenregeln für allgemeine Wurzeln")

st.markdown("Da sich alle Wurzeln auch als Potenzen schreiben lassen, kann man auch hier die bekannten Potenzrechenregeln anwenden:")

st.markdown("")
image_url = "https://i.postimg.cc/5NbCRzCs/02-01-Multiplizieren-von-allegemeinen-Wurzeln.jpg"
st.image(image_url)
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Multiplizieren von allgemeine Wurzeln](https://www.learningsnacks.de/share/380430/8499d9711316dfdf0f01017e8c62c77ebdea3304)")


st.markdown("")
image_url = "https://i.postimg.cc/PfmDyyPL/02-01-Dividieren-von-allegemeinen-Wurzeln.jpg"
st.image(image_url)
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Dividieren von allgemeine Wurzeln](https://www.learningsnacks.de/share/380567/69cc0c7c4a097b39d50131f1e6d8cc346158c443)")



st.markdown("")
image_url = "https://i.postimg.cc/KjrgYGd7/02-01-Mehrfach-verschachtelte-Wurzeln.jpg"
st.image(image_url)
st.markdown("")
st.markdown("")

col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Mehrfach verschachtelte Wurzeln](https://www.learningsnacks.de/share/380569/c4eb68c5f5679c6a08bccb0e6242f599997d1f72)")
