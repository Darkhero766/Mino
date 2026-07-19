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

        st.session_state.date = pd.read_csv(st.session_state.upload)

       # st.rerun()

    if st.button("Know it"):
        st.session_state.stage = "function"

    st.write(" ")

    if st.button("Read It"):
        st.session_state.stage = "read"

    st.write(" ")

    if st.button("Analize it "):
        st.session_state.stage = "analyse"


    

def read():
    st.subheader("Data")
    st.write(" ")
    #st.session_state.upload.see

    data = st.session_state.date

    st.dataframe(data)

    st.write(" ")

    if st.button("Return to Home"):
        st.session_state.stage = "home"

def analyse():
    st.header("Analysis")

    data = st.session_state.date
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
def function():
    st.header("How its Work")

    st.write(" ")

    st.subheader("1. Upload The csv Expense .")

    st.subheader("2. Its Scan the Copy (csv) then Finds the column 'Amount' .")

    st.write(" ")

    st.subheader("3. Read - It display Your Csv File .")

    st.write(" ")

    st.subheader("4. Analyse -  It reads csv , finds total sum , Total transaction,  and all")

    if st.button("Return To Home"):
        st.session_state.stage = "home"

    

if st.session_state.stage == "home":
    home()
elif st.session_state.stage == "read":
    read()

elif st.session_state.stage == "analyse":
    analyse()

elif st.session_state.stage == "function":
    function()


    
