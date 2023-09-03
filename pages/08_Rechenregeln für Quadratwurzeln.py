import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Rechenregeln für Quadratwurzeln")

st.latex(r"""\color{blue}\mathrm{\sqrt{a \cdot b}=\sqrt{a} \cdot \sqrt{b}}""")
st.latex(r"""\color{blue}\mathrm{\sqrt{\frac{a}{b}}=\frac{\sqrt{a}}{\sqrt{b}}}""")
st.latex(r"""\mathrm{\color{red} ACHTUNG!}""")
st.latex(r"""\mathrm{\color{red}Dies \: gilt\: nur\: für\: die\: Multiplikation\: und\: die\: Division,\: nicht\: aber\: für\: Addition\: und\: Subtraktion.}""")
st.latex(r"""\color{red}\mathrm{\sqrt{a + b}\neq \sqrt{a} + \sqrt{b}}""")
st.latex(r"""\color{red}\mathrm{\sqrt{a - b}\neq \sqrt{a} - \sqrt{b}}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Rechenregeln für Quadratwurzeln](https://www.learningsnacks.de/share/380428/97d1a6407b1bcc138a333aa42ab557077375aa64)")