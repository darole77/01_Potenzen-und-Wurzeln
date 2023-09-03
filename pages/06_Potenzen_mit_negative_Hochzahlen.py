import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Potenzen mit negativen Hochzahlen")

st.latex(r"""\color{blue}\mathrm{a^{-r}=\frac{1}{a^{r}}} \: \: \: \color{black}\mathrm{bzw.} \: \: \: \color{blue}\mathrm{\frac{1}{a^{-r}}=a^{r}}""")
st.markdown("Beispiel:")
st.latex(r"""\mathrm{5^{-2}=\frac{1}{5^{2}}} \: \: \: \mathrm{bzw.} \: \: \: \mathrm{\frac{1}{3^{-4}}=3^{4}}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Potenzen mit negativen Hochzahlen](https://www.learningsnacks.de/share/380426/b9c6c6e564b9f11b6492a0de6e52a45908b7953d)")