import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Quadratwurzel")

st.markdown("Das **Wurzelziehen** ist die **Umkehrung des Potenzierens**.")
st.latex(r"""\small\mathrm{Quadrieren: \: \: \color{blue}z \rightarrow z^{2}} """)
st.latex(r"""\small\mathrm{Wurzelziehen: \: \: \color{blue}\sqrt{z^{2}} \rightarrow z}""")
st.markdown("Die **Quadratwurzel** aus einer positiven Zahl $$\small\mathrm{a}$$ ist diejenige positive Zahl $$\small\mathrm{b}$$, die man mit sich selbst multiplizieren muss, um $$\small\mathrm{a}$$ zu erhalten.")
st.markdown("$$\small\mathrm{\sqrt{a}=b, \: wenn \: b^{2}=a} $$")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Quadratwurzel](https://www.learningsnacks.de/share/380427/2d032bc94eefc970b982a7e686b10000b97a781f)")