import streamlit as st
import string
import pickle as pkl
import numpy as np
import pandas

# model=pkl.load()
#
# def stemming(text):
#     text = text.lower()
#     a = text.split(" ")
#     p = []
#     for i in a:
#         i = "".join([j for j in i if j not in string.punctuation])
#         if i not in string.punctuation and i not in stopingWords:
#             p.append(ps.stem(i))
#     return " ".join(p)


# UI design

st.title("Fake news")
st.subheader("Check whether the news is fake or real 😶‍🌫️")
textarea = st.text_area("")

button= st.button("Predict")