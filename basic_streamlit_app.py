
import streamlit as st
import pandas as pd

st.header("Basic Foundation of Streamlit")
st.subheader("Elements are There ")
st.text("Your text is render here !")

# Data display
df = pd.DataFrame({"Date":["205-08-01","2025-07-01","2025-06-01"],
                   "Amount":[189,170,167]})
st.subheader("data display")
st.write("Here is a simple table ")
# st.table({"Column 1":[1,2,3,4], "Column 2":[5,6,7]})
st.table(df)


# Chart
st.subheader("Chart")
st.line_chart([1,2,3,4,5,6,7])
st.badge("Home", color="blue")

#user input

st.subheader("User input")

value = st.slider("select a value ",0,100)
st.write(f"Selected value {value}")











