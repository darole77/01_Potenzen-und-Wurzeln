{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d04ad4cc-35e5-4711-a265-2948a4a3b722",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from tabulate import tabulate\n",
    "from PIL import Image\n",
    "\n",
    "\n",
    "st.header(\"Die natürlichen Zahlen $$\\mathbb{N}$$\")\n",
    "st.markdown(\"[Learningsnack](https://www.learningsnacks.de/share/249432/c7b260eb380b35c7fa7b6072f4e2767f1a45bab3)\")\n",
    "st.markdown(\"Das Zählen ist die grundlegendste mathematische Tätigkeit und stand vermutlich auch im historischen Kontext am Anfang der Mathematik. Ausgehend von der Einheit (die Zahl $$\\small{1}$$) entstehen durch fortlaufendes Hinzufügen weiterer Einheiten die so genannten natürlichen Zahlen $$\\small{1, 2, 3, 4, 5, …}$$\")\n",
    "    \n",
    "image_url = \"https://imageshack.com/i/pm5BDdqup\"\n",
    "st.image(image_url)\n",
    "       \n",
    "st.markdown(\"Die Menge der natürlichen Zahlen wird in der Mathematik mit dem Symbol N bezeichnet und man schreibt: \")\n",
    "st.latex(r\"\\mathbb{N} = \\lbrace 1; 2; 3; 4; 5; ... \\rbrace\")\n",
    "st.markdown(\"Dabei symbolisieren die drei Punkte $$„…“$$, dass es immer in dieser Form weitergeht, ohne jemals abzubrechen. Die natürlichen Zahlen lassen sich als Punkte am so genannten Zahlenstrahl veranschaulichen. Die Zahl 0 wird normalerweise nicht zu den natürlichen Zahlen gezählt. Möchte man die Zahl 0 dabeihaben, so schreibt man in der Regel: \")\n",
    "st.latex(r\"\\mathbb{N}_{0} = \\lbrace 1; 2; 3; 4; 5; ... \\rbrace\")\n",
    "    \n",
    "st.markdown(\"Die natürlichen Zahlen lassen sich am so genannten 'Zahlenstrahl' darstellen: \")\n",
    "image_url = \"https://imageshack.com/i/pomGWAZ5p\"\n",
    "st.image(image_url)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
