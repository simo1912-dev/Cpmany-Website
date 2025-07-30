import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("COntact Us")
st.write("We’d love to hear from you. Please fill out the form below:")
name = st.text_input("Your name")
email = st.text_input("Your email")
message = st.text_area("Your message")

if st.button("Send"):
    if name and email and message:
        st.success("Your message hjas been sent")
    else:
        st.error("Please fill all the fields before submitting")