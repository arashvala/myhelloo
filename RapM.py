import streamlit as st
st.write("Hiiiiiiiiiii SHABNAM")


with st.sidebar:
    st.title('Train Dynamic Simulation')
    st.image(
        "https://www.euspa.europa.eu/sites/default/files/files/content/news/images/home/alstom.jpg",
        width=280,  # Manually Adjust the width of the image as per requirement
    )
    st.header('Please Enter The Input Data:')
  
number = st.slider("Pick a number: ", min_value=1, max_value=10)
st.text("Your number is " + str(number))
