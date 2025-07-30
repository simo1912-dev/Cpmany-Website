import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("The best company in germany")
st.write("""We are committed to delivering innovative solutions and exceptional service, 
helping businesses grow and succeed in a rapidly changing world.”

Would you like me to also suggest 3 company values or a short tagline to 
make the page look more complete?
""")

st.markdown("## Our Team")
col1, emp1, col2, emp2, col3 = st.columns([1.5, 0.5, 1.5, 0.5, 1.5])

# now lets read the csv files
data = pd.read_csv("data.csv")
with col1:
    for index, row in data[:5].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col2:
    for index, row in data[5:9].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in data[9:].iterrows():
        st.header(f"{row['first name']} {row['last name']}")
        st.write(row["role"])
        st.image("images/" + row["image"])