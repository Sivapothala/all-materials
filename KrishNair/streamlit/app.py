import streamlit as st
import pandas as pd
import numpy as np


##titile of the application
st.title("Welcome to Streamlit")

## Display simple text
st.text("This is a sample Text")

## Create Sample DataFrame
df = pd.DataFrame({
    'first' : [1,2,3,4],
    'second' : [4,6,5,7]
     })

st.write("Here is the DataFrame")
st.write(df)


## create a Line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)