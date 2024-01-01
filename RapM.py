import streamlit as st
import numpy as np
import pandas as pd


st.header("Hiiiiiiiiiii babababa")


with st.sidebar:
    F1 = st.number_input('Insert First Frequency:', min_value=1, max_value=40, step=1)

with st.sidebar:
    F2 = st.number_input('Insert Second Frequency:', min_value=1, max_value=40, step=1)

with st.sidebar:
    F3 = st.number_input('Insert Thirth Frequency:', min_value=1, max_value=40, step=1)

with st.sidebar:
    F4 = st.number_input('Insert Fourth Frequency:', min_value=1, max_value=40, step=1)

with st.sidebar:
    Time = st.number_input('Insert Time:', min_value=1, max_value=100, step=1)


Xt= np.arange(0, Time, 0.01)
Yt= np.sin(F1*Xt)+np.sin(F2*Xt)+np.sin(F3*Xt)+np.sin(F4*Xt)

chart_data = pd.DataFrame(Yt)

st.area_chart(chart_data)
