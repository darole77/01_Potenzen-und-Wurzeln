import streamlit as st
import numpy as np
import pandas as pd
from tabulate import tabulate
from PIL import Image


st.header("Die reellen Zahlen $$\mathbb{R}$$")
st.markdown("Obwohl die rationalen Zahlen (Brüche) „dicht“ auf der Zahlengeraden liegen (das heißt, dass zwischen zwei beliebigen rationalen Zahlen immer noch unendlich viele weitere rationale Zahlen liegen) decken sie noch nicht alle Punkte der Zahlengerade ab. Es gibt auf der Zahlengerade **„Lücken“**, die nicht von rationalen Zahlen eingenommen werden können. ")
st.markdown("Beispielsweise lässt sich die Zahl $$\sqrt{2}$$ ganz einfach auf der Zahlengerade darstellen, indem man die Länge der Diagonale des Einheitsquadrats (Quadrat mit der Seitenlänge 1) mit dem Zirkel auf die Zahlengerade abschlägt: ")
image_url = "https://imageshack.com/i/pon5LGDcj"
st.image(image_url)
    
st.markdown("Die Zahl $$\sqrt{2}$$ **lässt sich aber NICHT als Bruch darstellen**, ist also keine rationale Zahl, was bereits die Griechen in der Antike herausgefunden haben. Und wenn man die Zahl $$\sqrt{2}$$ als Dezimalzahl angeben möchte ($$\sqrt{2}≈1,414213562$$), so ergibt sich ein unendlich langer Dezimalbruch, der allerdings **niemals periodisch wird**.")
st.markdown("Zahlen, die diese Eigenschaft erfüllen (**nicht periodische Dezimalzahlen mit unendlich vielen Nachkommastellen**), nennt man **irrationale Zahlen**. Weiter Beispiele für irrationale Zahlen sind $$\sqrt{3}$$, $$\sqrt{5}$$, $$\sqrt{7}$$ , … oder aber beispielsweise auch die Kreiszahl $$\pi$$.")
st.markdown("Auf der Zahlengerade liegen also offensichtlich Punkte, die nicht von den rationalen Zahlen (Brüchen) eingenommen werden können. Diese Lücken werden von den **irrationalen Zahlen** gefüllt, womit nun wirklich jedem Punkt, der auf der Zahlengerade liegt, auch eine Zahl zugeordnet werden kann. ")
st.markdown("Den Zahlenbereich, der dadurch entsteht, nennt man **reelle Zahlen**.")
st.markdown("Die reellen Zahlen setzen sich also zusammen aus den **rationalen Zahlen (Zahlen die als Bruch darstellbar sind)** und den **irrationalen Zahlen (nicht periodische Dezimalbrüche mit unendlich vielen Nachkommastellen)** In der Mathematik bezeichnet man die reellen Zahlen mit dem Symbol $$\mathbb{R}$$")
st.markdown("")
image_url = "https://imageshack.com/i/poPtOkVij"
st.image(image_url)
st.write("")
st.write("")
image_url = "https://imageshack.com/i/poOzIfsHj"
st.image(image_url)

st.markdown("[Learningsnack zu den reellen Zahlen](https://www.learningsnacks.de/share/253361/cd70bf896e05b1bd1b85de456cb619e23f0ca118")