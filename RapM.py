import streamlit as st
st.write("Hiiiiiiiiiii")
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
