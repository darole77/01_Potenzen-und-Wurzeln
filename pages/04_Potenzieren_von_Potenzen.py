import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Potenzieren von Potenzen")
st.markdown("Eine Potenz wird **potenziert**, indem man **die Exponenten multipliziert**.")
st.latex(r"""\color{blue}\mathrm{(a^{r})^{s}=a^{r \cdot s}}""")
st.markdown("Beispiel:")
st.latex(r"""\mathrm{(3^{2})^{4}=3^{2 \cdot 4}=3^{8}}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Potenzieren von Potenzen](https://www.learningsnacks.de/share/380397/32ba0fab788f0fc9a6f030836a5648994244ff2a)")