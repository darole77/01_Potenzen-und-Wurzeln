import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Teilbarkeit")
st.markdown("Die Teilbarkeit ist eine wichtige Eigenschaft der natürlichen Zahlen. Sie wird in der Mathematik folgendermaßen definiert:")
st.markdown("Man sagt „Die Zahl $$a$$ ist Teiler von $$b$$“ oder „$$b$$ ist durch $$a$$ teilbar“, wenn es zu den natürlichen Zahlen $$a$$ und $$b$$ eine natürliche Zahl $$c$$ gibt, sodass gilt:")
st.latex(r"b=a⋅c")
st.markdown("Wenn $$a$$ Teiler von $$b$$ ist, so schreibt man: $$a | b$$   andernfalls  $$a ∤ b$$")
    
st.markdown("Beispiele:")
data = {
    "Aussage": ["$$\small\mathrm{3 \: ist \: \color{green}ein \: \color{black}Teiler \: von \: 12}$$", 
                "$$\small\mathrm{3 \: ist \: \color{red}nicht \: \color{black}Teiler \: von \: 14}$$", 
                "$$\small\mathrm{5 \: ist \: \color{green}ein \: \color{black}Teiler \: von \: 65}$$",
                "$$\small\mathrm{6 \: ist \: \color{red}nicht \: \color{black}Teiler \: von \: 32}$$"],
    "Begründung": ["$$\small\mathrm{... \: weil \: es \: \color{green}eine \: \color{black}natürliche \: Zahl \: gibt \: (4), \: sodass \: gilt: 12=3 \cdot 4}$$", 
                   "$$\small\mathrm{... \: weil \: es \: \color{red}keine  \: \color{black}natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 14=3 \cdot c}$$",
                   "$$\small\mathrm{... \: weil \: es \: \color{green}eine \: \color{black}natürliche \: Zahl \: gibt \: (13), \: sodass \: gilt: 65=5 \cdot 13}$$",
                   "$$\small\mathrm{... \: weil \: es \: \color{red}keine \: \color{black}natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 32=6 \cdot c}$$"],
    "Formale Schreibweise":["$$\small\mathrm{3 \mid 12}$$", 
                            "$$\small\mathrm{3 ∤ 14}$$",
                            "$$\small\mathrm{5 \mid 65}$$",
                            "$\small\mathrm{6 ∤ 32}$"],}
df = pd.DataFrame(data)
md_df = df.to_markdown(index=False)
st.markdown(md_df, unsafe_allow_html=True)
    
st.markdown("")
st.markdown("")
st.markdown("Teilbarkeit durch 0:")
data = {
    "Aussage": ["$$\small\mathrm{0 \: ist \: kein \: Teiler \: von \: 1}$$", 
                "$$\small\mathrm{0 \: ist \: kein \: Teiler \: von \: 2}$$", 
                "$$\small\mathrm{0 \: ist \: kein \: Teiler \: von \: 3}$$",
                "$$\small\mathrm{...}$$"],
    "Begründung": ["$$\small\mathrm{... \: weil \: es \: keine \: natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 1=0 \cdot c}$$", 
                   "$$\small\mathrm{... \: weil \: es \: keine \: natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 2=0 \cdot c}$$",
                   "$$\small\mathrm{... \: weil \: es \: keine \: natürliche \: Zahl \: c \: gibt, \: sodass \: gilt: 3=0 \cdot c}$$",
                   "$$\small\mathrm{...}$$"],
    "Formale Schreibweise":["$$\small\mathrm{0 ∤ 1}$$", 
                            "$$\small\mathrm{0 ∤ 2}$$",
                            "$$\small\mathrm{0 ∤ 3}$$",
                            "$\small\mathrm{...}$"],}
df = pd.DataFrame(data)
md_df = df.to_markdown(index=False)
st.markdown(md_df, unsafe_allow_html=True)
    
st.markdown("")
st.markdown("Da eine Multiplikation mit 0 als Ergebnis immer 0 liefert, kann die Zahl 0 selbst niemals Teiler einer anderen Zahl sein. Durch 0 zu teilen, ergibt also mathematisch keinen Sinn und wird daher in der Mathematik nicht erlaubt (nicht definiert).")

st.markdown("[Learningsnack zur Teilbarkeit](https://www.learningsnacks.de/share/249449/419f2eb476c8f619d4f1e3f64a6c8d76d0f19805)")