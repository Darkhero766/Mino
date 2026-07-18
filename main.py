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
    #st.session_state.upload.see

    date = pd.read_csv(st.session_state.upload)

    st.dataframe(date)

    st.write(" ")

    if st.button("Return to Home"):
        st.session_state.stage = "home"

def analyse():
    st.header("Analysis")

    data = pd.read_csv(st.session_state.upload)
    st.write(" ")

    column = "amount"

    

    data.columns = data.columns.str.lower()

    data[column] = pd.to_numeric(data[column])
    
    if column.lower() in data.columns:

        total = data[column].sum()

        st.write(" ")

        average = data[column].mean()

        st.metric("Total Transaction", f"{len(data[column])}")

        st.write(" ")

        st.metric(f"Total Amount Spent :", f"{total}")

        st.write(" ")

        st.metric(f"Avrage Expense :", f"{average:.2f}")
        st.write(" ")

        


    else:
        st.write("Column Not Found")

    st.write(" ")

    if st.button("Return To Home"):
        st.session_state.stage = "home"
def draw():
    pass 

if st.session_state.stage == "home":
    home()
elif st.session_state.stage == "read":
    read()

elif st.session_state.stage == "analyse":
    analyse()

    
