import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image




st.header("Vom Zählen zum Rechnen")
st.markdown("Über das **Zählen** gelangt man irgendwann zwangsläufig zum **Rechnen**.")
st.markdown("Beispiel:")
st.markdown("Zähle zunächst die Dinge in jedem der vier untenstehenden Bilder. Überlege dir anschließend, wie du vorgegangen bist. ")
image_url = "https://imageshack.com/i/poiWHaJRj"
st.image(image_url)
st.markdown("Das **Bündeln in Gruppen** ist eine einfache und naheliegende **Zählstrategie**. Man braucht nicht mehr alle Objekte einzeln zu zählen, sondern fasst sie in Gruppen zusammen. Von hier ist es dann nur noch ein kleiner Schritt zur ersten Rechenoperation, der **Addition** (Plusrechnung). Wenn man beispielsweise die Anzahl der Dinge im zweiten Bild (rechts oben) durch $$\small{3+3+5=11}$$ ermittelt hat, dann hat man genau diese Zähl-Strategie angewendet und ist dadurch direkt vom Zählen zum Addieren übergegangen. Das Bündeln in Gruppen ist eine einfache und naheliegende Zählstrategie. Man braucht nicht mehr alle Objekte einzeln zu zählen, sondern fasst sie in Gruppen zusammen. Von hier ist es dann nur noch ein kleiner Schritt zur ersten Rechenoperation, der Addition (Plusrechnung). Wenn man beispielsweise die Anzahl der Dinge im zweiten Bild (rechts oben) durch $$\small{3+3+5=11}$$ ermittelt hat, dann hat man genau diese Zähl-Strategie angewendet und ist dadurch direkt vom **Zählen zum Addieren** übergegangen. ")
st.markdown("Wenn die Objekte in günstigen Mustern angeordnet sind (z.B. Reihen und Spalten), dann kann man ihre Anzahl auch durch **Multiplikation** (Malrechnung) ermitteln. Im dritten Bild (links unten) die Anzahl ermitteln, indem man $$\small{2\cdot5=10}$$ rechnet. ")
st.markdown("Wenn man im vierten Bild (rechts unten) die Anzahl beispielsweise über $$\small{3\cdot5-1=14}$$ ermittelt hat, so hat man bereits eine Kombination aus verschiedenen Rechenoperationen angewendet.")
st.markdown("Die **Addition (+)** ist also eine naheliegende Weiterentwicklung des Zählens und die **Multiplikation (∙)** ist eine Weiterentwicklung der Addition. Gemeinsam mit den zugehörigen Umkehroperationen **Subtraktion (–)** und **Division (:)** ergeben sich die **vier Grundrechenarten** der Arithmetik.")

st.markdown("[Learningsnack Vom Zählen zum Rechnen](https://www.learningsnacks.de/share/249439/b199312900464215526ef7a8bd0b3856c5369f6e )")