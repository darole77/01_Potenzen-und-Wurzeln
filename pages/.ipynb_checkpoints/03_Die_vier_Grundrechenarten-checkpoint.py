import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image

st.header("Die vier Grundrechenarten")
   
st.subheader("Addition")
st.markdown("Beim **$$\mathrm{\color{green}{Addieren}}$$** werden Zahlen zusammengezählt. Das hierfür verwendete Symbol (Rechenzeichen) ist das Pluszeichen (+).")
st.latex(r"\begin{matrix}12&+&3&=&15\\ & & & & \\ \mathrm{\color{blue}{Summand}}&\mathrm{plus}&\mathrm{\color{blue}{Summand}}&\mathrm{gleich}&\mathrm{\color{blue}{Summe}}\end{matrix}")

st.subheader("Multiplikation")
st.markdown("Beim **$$\mathrm{\color{green}{Multiplizieren}}$$** werden Zahlen vervielfacht. Das hierfür verwendete Symbol (Rechenzeichen) ist das Malzeichen (∙).")
st.latex(r"\begin{matrix}12&\cdot&3&=&36\\ & & & & \\\mathrm{\color{blue}{Faktor}}&\mathrm{mal}&\mathrm{\color{blue}{Faktor}}&\mathrm{gleich}&\mathrm{\color{blue}{Produkt}}\end{matrix}") 

st.subheader("Subtraktion")
st.markdown("Beim **$$\mathrm{\color{green}{Subtrahieren}}$$** wird eine Zahl von einer anderen abgezogen. Das hierfür verwendete Symbol (Rechenzeichen) ist das Minuszeichen (–).")
st.latex(r"\begin{matrix}12&-&3&=&9\\ & & & & \\\mathrm{\color{blue}{Minuend}}&\mathrm{minus}&\mathrm{\color{blue}{Subtrahend}}&\mathrm{gleich}&\mathrm{\color{blue}{Differenz}}\end{matrix}")

st.subheader("Division")
st.markdown("Beim **$$\mathrm{\color{green}{Dividieren}}$$** werden Zahlen geteilt. Das hierfür verwendete Symbol (Rechenzeichen) ist das Geteilt-Zeichen (:).")
st.latex(r"\begin{matrix}12&:&3&=&4\\ & & & & \\ \mathrm{\color{blue}{Dividend}}&\mathrm{durch}&\mathrm{\color{blue}{Divisor}}&\mathrm{gleich}&\mathrm{\color{blue}{Quotient}}\end{matrix}")
    
st.markdown("")
st.markdown("")
st.markdown("")
st.subheader("Vorrangregeln")
st.markdown("Die Rechenoperationen **$$\mathrm{\color{green}{Addition}}$$** und **$$\mathrm{\color{green}{Subtraktion}}$$** bezeichnet man als **$$\mathrm{\color{green}{Strichrechenarten}}$$** (+ und –). Sie gelten als Rechenarten erster Stufe.")
st.markdown("Die Rechenoperationen **$$\mathrm{\color{blue}{Multiplikation}}$$** und **$$\mathrm{\color{blue}{Division}}$$** bezeichnet man als **$$\mathrm{\color{blue}{Punktrechenarten}}$$** (∙ und :). Sie gelten als Rechenarten zweiter Stufe.")
st.markdown("Für die Reihenfolge der Rechenoperationen gilt:")
st.markdown("1. Kommen in einer Rechnung ausschließlich Rechenarten derselben Stufe vor, so wird **$$\mathrm{\color{red}{\: von \: links \: nach \: rechts \:}}$$** gerechnet.")
st.markdown("2. Kommen in einer Rechnung Rechenarten unterschiedlicher Stufe und eventuell auch Klammern vor, so gilt: **$$\mathrm{\color{red}{\: Klammer \: vor \: Punkt \: vor \: Strich! \:}}$$**")

st.markdown("[Learningsnack zu den Grundrechenarten](https://www.learningsnacks.de/share/249445/fb6f9b7e0833dce4405c2deaaabfa790c362aa56)")