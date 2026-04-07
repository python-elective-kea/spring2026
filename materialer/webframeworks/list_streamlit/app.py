import streamlit as st
import pandas as pd
import numpy as nppyt

st.title('Uber pickups in NYC')
st.markdown('FFFFFFF')

col1,col2= st.columns(2)

with col1: 
    num = st.slider('slider',1,10,2)
with col2: 
    f'{num}'

    