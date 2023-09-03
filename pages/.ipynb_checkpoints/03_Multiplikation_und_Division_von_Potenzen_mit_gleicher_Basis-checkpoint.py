import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Multiplikation und Division von Potenzen mit gleicher Basis")
st.markdown("Potenzen **mit derselben Basis** werden **multipliziert**, indem man die **Exponenten addiert** und die **Basis unverändert** lässt.")
st.latex(r"""\color{blue}\mathrm{a^{r} \cdot a^{s} = a^{r+s}}""")
st.markdown("Beispiel:")
st.latex(r"""\mathrm{3^{2} \cdot 3^{4}=3^{2+4}=3^{6}}""")
st.markdown("")
st.markdown("Potenzen **mit derselben Basis** werden **dividiert**, indem man die **Exponenten subtrahiert** und die **Basis unverändert** lässt.")
st.latex(r"""\color{blue}\mathrm{\frac{a^{r}}{a^{s}}=a^{r-s}}""")
st.latex(r"""\mathrm{\frac{3^{4}}{3^{2}}=3^{4-2}=3^{2}}""")
