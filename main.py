import streamlit as st
import pandas as pd
import time

stage = "home"

if "stage" not in st.session_state:
    st.session_state.stage = "home"


st.title(" Mino ")
st.write(" ")



def home():

    st.header("Track Expenses")
    st.write(" ")

    files = st.file_uploader("Upload CSV ", type=["csv"])
    st.write(" ")

    if files is not None:
   #     st.session_state.stage = "read"

        st.session_state.upload = files
       # st.rerun()

    if st.button("Read It"):
        st.session_state.stage = "read"

    st.write(" ")

    if st.button("Analize it "):
        st.session_state.stage = "analyse"


    

def read():
    st.subheader("Data")
    st.write(" ")

    date = pd.read_csv(st.session_state.upload)

    st.dataframe(date)

def analyse():
    st.header("Analysis")

    data = pd.read_csv(st.session_state.upload)
    st.write(" ")

    column = "Amount"
    if column.lower() in data.columns:

        total = data[column].sum()

        st.write(total)
    else:
        st.write("Column Not Found")


if st.session_state.stage == "home":
    home()
elif st.session_state.stage == "read":
    read()

elif st.session_state.stage == "analyse":
    analyse()

    
