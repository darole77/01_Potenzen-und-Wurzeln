import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Die ganzen Zahlen $$\mathbb{Z}$$")
st.markdown("Fügt man den **natürlichen Zahlen** auch die entsprechenden **negativen Zahlen** hinzu, so erhält man die **Menge der ganzen Zahlen**. Man schreibt:")
st.latex(r"\mathbb{Z} = \lbrace ...; -5; -4; -3; -2; -1;\quad 0;\quad 1; \quad 2; \quad 3; \quad 4; \quad 5; ... \rbrace")
st.markdown("Die ganzen Zahlen lassen sich als Punkte auf der **Zahlengeraden** veranschaulichen.")
image_url = "https://imageshack.com/i/pnxbw6Puj"
st.image(image_url)
st.markdown("Vor negative Zahlen schreibt man ein **Minuszeichen**, wobei zu beachten ist, dass es sich hierbei nicht um ein „Rechenzeichen-Minus“ handelt, sondern um ein **„Vorzeichen-Minus“**. ")

st.markdown("[Learningsnack zu den ganzen Zahlen](https://www.learningsnacks.de/share/249464/ddf54e882cc39fee7a09ffd95a814a5ab6a2d9d7)")