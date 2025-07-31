import streamlit as st
import pandas as pd
from send_email import send_email

st.set_page_config(layout="wide")
st.title("Contact Us")
st.write("We’d love to hear from you. Please fill out the form below:")
name = st.text_input("Your name")
email = st.text_input("Your email")
message = st.text_area("Your message")

if st.button("Send"):
    if name and email and message:
        send_email(message, email)
        st.info("Your email was sent successfully")
    else:
        st.error("Please fill all the fields before submitting")
