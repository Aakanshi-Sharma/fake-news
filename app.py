import streamlit as st
import string
import time
import pickle as pkl
import numpy


model = pkl.load(open("model.pkl", "rb"))
ps = pkl.load(open("portStem.pkl", "rb"))
stopingWords = pkl.load(open("stoping.pkl", "rb"))
vectorizer = pkl.load(open("vectorizer.pkl", "rb"))


def stemming(text):
    text = text.lower()
    a = text.split(" ")
    p = []
    for i in a:
        i = "".join([j for j in i if j not in string.punctuation])
        if i not in string.punctuation and i not in stopingWords:
            p.append(ps.stem(i))
    return " ".join(p)


def predicting(content):
    content = stemming(content)
    content = numpy.array(content, ndmin=1)
    content = vectorizer.transform(content)
    y_pred = model.predict(content)
    print(y_pred)
    return y_pred


# UI design
title = '<h1 style="border-bottom: 2px solid white" >Fake News Detection</h1>'
st.markdown(title, unsafe_allow_html=True)
st.subheader("Check whether the news is fake or real 😶‍🌫️")

textarea = st.text_area("")

clicked = st.button("Predict")
if clicked:
    result = predicting(textarea)
    real_news = '<p style="color:#33cc33; font-weight:700; font-size: 30px;">Real News</p>'
    fake_news = '<p style="color:red; font-weight:700; font-size: 30px;">Fake News</p>'
    with st.spinner('Wait for it...'):
        time.sleep(1)
    if result[0] == 0:
        st.markdown(real_news, unsafe_allow_html=True)
        st.snow()
    else:
        st.markdown(fake_news, unsafe_allow_html=True)
