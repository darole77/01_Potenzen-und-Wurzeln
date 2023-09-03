import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Der allgemeine Wurzelbegriff")

st.markdown("Das **Wurzelziehen** ist die **Umkehrung des Potenzierens**.")
st.latex(r"""\color{blue}\mathrm{2^5=32 \: \rightarrow \: \sqrt[5]{32}=2}""")
st.latex(r"""\color{blue}\mathrm{3^4=81 \: \rightarrow \: \sqrt[4]{81}=3}""")
st.markdown("Allgemein:")
st.markdown("Die **$$\mathrm{n}$$-te Wurzel** aus einer positiven Zahl $$\mathrm{a}$$ (geschrieben $$\mathrm{\sqrt[n]{a}}$$ ) ist diejenige positive Zahl, deren $$\mathrm{n}$$-te Potenz gleich $$\mathrm{a}$$ ist.")

st.markdown("Bezeichnungen:")
image_url = "https://i.postimg.cc/gkwtCRrG/02-01-Allgemeine-Wurzeln-01-jpg.gif"
st.image(image_url, width=350)
st.markdown("")
st.markdown("")
st.markdown("Beispiele:")
st.latex(r"""\mathrm{\sqrt[3]{8}=2, \: weil \: 2^{3}=8}""")
st.latex(r"""\mathrm{\sqrt[4]{81}=3, \: weil \: 3^{4}=81}""")
st.markdown("")
st.markdown("")
st.markdown("Jede Wurzel kann **als Potenz mit rationalem Exponenten** (Hochzahl als Bruch) geschrieben werden.")
st.latex(r"""\color{blue}\mathrm{\sqrt[n]{a}=a^{\frac{1}{n}}}""")
st.latex(r"""\color{blue}\mathrm{\sqrt[n]{a^m}=a^{\frac{m}{n}}}""")
st.markdown("")
st.markdown("")
st.markdown("Beispiele:")
st.latex(r"""\mathrm{\sqrt[4]{x}=x^{\frac{1}{4}}}""")
st.latex(r"""\mathrm{\sqrt[5]{y^3}=y^{\frac{3}{5}}}""")

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Der allgemeine Wurzelbegriff](https://www.learningsnacks.de/share/380429/75cd18b3b27c2cd38210b7aa21e4a98a19a84374)")
