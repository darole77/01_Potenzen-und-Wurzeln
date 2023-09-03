import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Potenzen")
st.markdown("Ausdrücke der Form **$$\color{blue}\small\mathrm{a^n}$$** heißen **Potenzen**. Dabei wird $$\small\mathrm{a}$$ als **Basis** und $$\small\mathrm{n}$$ als **Exponent** oder **Hochzahl** bezeichnet. Die Rechenoperation heißt **Potenzieren** und ist eine **Rechenoperation dritter Stufe** (sie hat also Vorrang vor den Punkt – und den Strichrechenarten).")
st.markdown("Beispiele:")
st.latex(r"""\mathrm{4^{2} = 4 \cdot 4}""")
st.latex(r"""\mathrm{2^{3} = 2 \cdot 2 \cdot 2}""")
st.latex(r"""\mathrm{5^{4}=5 \cdot 5 \cdot 5 \cdot 5}""")

st.markdown("")
st.markdown("Weiters gilt:")
st.latex(r"""\color{blue}\mathrm{a^{1}=a}""")
st.latex(r"""\color{blue}\mathrm{a^{0}=1}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Potenzen](https://www.learningsnacks.de/share/380255/76fdd0eaa36d2fd0bc3b417dd991f277d1e7498d)")