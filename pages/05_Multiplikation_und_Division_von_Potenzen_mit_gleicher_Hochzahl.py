import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Multiplikation und Division von Potenzen mit gleicher Hochzahl")

st.latex(r"""\color{blue}\mathrm{a^{n} \cdot b^{n}=(a \cdot b)^{n}}""")
st.markdown("Beispiel:")
st.latex(r"""\mathrm{3^{2} \cdot 4^{2}=(3 \cdot 4)^{2}=12^{2}}""")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.latex(r"""\color{blue}\mathrm{\frac{a^{n}}{b^{n}}=\left(\frac{a}{b}\right)^{n}}""")
st.markdown("Beispiel:")
st.latex(r"""\mathrm{\frac{20^{2}}{5^{2}}=\left(\frac{20}{5}\right)^{2}=4^{2}}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Multiplikation und Division von Potenzen mit gleicher Hochzahl](https://www.learningsnacks.de/share/380400/05463b4539cfb4f2700894121b684b8ed5d2cbea)")