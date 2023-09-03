import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Die rationalen Zahlen $$\mathbb{Q}$$")
st.markdown("Fügt man den **ganzen Zahlen** nun auch noch die **positiven und negativen Brüche** hinzu, so erhält man die **Menge der rationalen Zahlen**. Dies sind alle Zahlen, die sich als Bruch darstellen lassen, also in der Form $$p \over q$$ (wobei $$p$$ und $$q$$ hier für beliebige ganze Zahlen stehen können, $$q$$ allerdings nicht 0 sein darf).")
st.markdown("Die formale Darstellung dieser Zahlenmenge lautet:")
st.latex(r"\mathbb{Q} = \lbrace {p \over q} | p, q ∈ \mathbb{Z}; q≠ 0 \rbrace")
st.markdown("Auch jeder rationalen Zahl kann ein Punkt auf der **Zahlengeraden** zugeordnet werden:")
image_url = "https://imageshack.com/i/pmir77I3j"
st.image(image_url)
st.markdown("Die rationalen Zahlen liegen dabei „dicht“ auf der Zahlengeraden, das heißt, dass es zwischen zwei rationalen Zahlen immer noch unendlich viele weitere rationale Zahlen gibt.")
st.markdown("Hier zur Veranschaulichung ein paar Beispiele für rationale Zahlen:  ")
image_url = "https://imageshack.com/i/pmuSW5mej"
st.image(image_url)

st.markdown("[Learningsnack](https://www.learningsnacks.de/share/251227/3f43c74795debbed212cc2e17f94599ce171aee0)")