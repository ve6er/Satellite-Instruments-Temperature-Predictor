import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pickle

st.markdown("<h1 style='text-align: center; font-family: Roboto;'>Spacecraft Instrument Temperature Predictor</h1>", unsafe_allow_html=True)
st.image(Image.open("satellite.jpg"), caption="Image taken from https://www.peakpx.com/")
st.markdown("<h1 style='text-align: left; font-family: Roboto; font-size: 30px;'>About</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; font-family: Roboto; font-size: 25px;'>Knowing the performance of your instrument is vital for deep space exploration. It affects the type of material needed, the range of safe operating conditions etc. Furthermore, when an instrument is launched into space, and some error is discovered, one cannot simply take it back down, make the necessary changes and send it back up. Therefore, it is absolutely crucial to know the temperature of the instruments under various operating conditions before sending them into space.</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; font-family: Roboto; font-size: 25px;'>Here it is important to not that the data has been taken from the Chandrayaan-2 Orbitor and the predictions are therefore, only valid for lunar satellites for the time being.</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; font-family: Roboto;'></h1>", unsafe_allow_html=True)

sr1= st.slider("Enter the value of the current in sensor 1 (in mA)", min_value=0.0, max_value=1.6, value=1.2)
sr2= st.slider("Enter the value of the current in sensor 2 (in mA)", min_value=0.0, max_value=1.2, value=0.8)
f1= st.slider("Enter the value of focus 1", min_value=-25.00, max_value=25.00, value=-19.7)
ra= st.slider("Enter the value of Roll Angle", min_value=0.0, max_value=180.0, value= 0.1)
fc= st.slider("Enter the value of the filament current (in A)", min_value=-8.00, max_value=2.40, value=2.2)
psv= st.slider("Enter the power supply voltage (in V)", min_value=0.00, max_value=30.00, value=24.5)

listt=[sr1, sr2, f1, fc, ra, psv]
vk= np.array(listt).reshape(1, 6)
model=pickle.load(open("temperature_predictor.pkl", "rb"))
temp=float(model.predict(vk))
a=f"{temp}"
if temp<-271.15:
    temp=271.15
    a=f"{temp}"+chr(176)+'C'
else:
    if temp< 0:
        if temp<=-100:
            a=a[:7]+chr(176)+'C'
        else:
            a=a[:6]+chr(176)+'C'
    else:
        a=a[:-12]+chr(176)+'C'
st.markdown("<h1 style='text-align: left; font-family: Roboto; font-size: 22px;'>Approximated temperature of the electronics under these working conditions:</h1>", unsafe_allow_html=True)
st.markdown(f"<h1 style='text-align: center; font-family: Roboto; font-size: 30px;'>{a}</h1>", unsafe_allow_html=True)
