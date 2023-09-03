import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image




st.header("Addition und Subtraktion von Potenzen")
st.markdown("Potenzen können genau dann **addiert** bzw. **subtrahiert** werden, wenn **sowohl ihre Basen als auch ihre Exponenten übereinstimmen**.")
st.markdown("Beispiel:")
image_url = "https://i.postimg.cc/L64fZ7hy/02-01-Addieren-und-Subtrahieren.jpg"
st.image(image_url, width=250)

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
col1, col2 = st.columns(2)
with col1:
    image_url = "https://i.postimg.cc/m2xLjR7y/Logo-LS.jpg"
    st.image(image_url, width=200)
with col2:
    st.markdown("[Addition und Subtraktion von Potenzen](https://www.learningsnacks.de/share/380267/a03575ac6b0468b89f473e8ff35a7b2c643645c0)")

