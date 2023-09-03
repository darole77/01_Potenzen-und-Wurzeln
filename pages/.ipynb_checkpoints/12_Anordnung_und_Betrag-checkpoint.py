import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Anordnung und Betrag")
st.markdown("Wenn man zwei Zahlen **ihrer Größe nach vergleichen** will, so geht man wie bei einem Temperaturvergleich vor: Die Temperatur $$-5° C$$ ist kleiner als $$-2° C$$.")
st.markdown("Entsprechend ist $$-5$$ kleiner als $$-2$$.")
st.markdown("Man schreibt dafür:")
st.markdown("$$-5<-2")
st.markdown("Zahlen lassen sich ganz leicht vergleichen, wenn man sie auf der Zahlengeraden darstellt.")
image_url = "https://imageshack.com/i/pnaHIADsj"
st.image(image_url)
  
st.markdown("Von zwei Zahlen ist diejenige die kleinere, die auf der Zahlengeraden weiter links liegt.")
st.markdown("")
st.markdown("")
st.markdown("Die Zahlen $$-3$$ und $$3$$ sind auf der Zahlengeraden gleich weit von der $$0$$ entfernt. Man bezeichnet sie als **Gegenzahlen**.")
image_url = "https://imageshack.com/i/pottxxdAj"
st.image(image_url)
    
    
st.markdown("Der **Abstand einer Zahl von der Zahl $$0$$** wird als **Betrag** bezeichnet. Das mathematische Symbol für den Betrag ist $$| \quad | $$")
st.markdown("Es gilt also:")
st.latex(r"\begin{matrix} |3|=3& bzw. &|-3|=3\\ \\ \end{matrix}") 
    
st.markdown("Eine Zahl und ihre Gegenzahl haben stets denselben Betrag.")

st.markdown("[Learningsnack zu Anordnung und Betrag](https://www.learningsnacks.de/share/254800/4bf428b82da3ab3d266ee2bf2a4ce83c3de7853f")