import streamlit as st
import pandas as pd


st.title("Streamlit widgets")

name = st.text_input("Enter yout name ")

age = st.slider("Slect your age ",0,100,35)


options =['Python','java','c']
choices = st.selectbox("Choose the favorite language",options)
st.write(f"you selected {choices}")
st.write(f"your age is {age}")

if name:
    st.text(f"Hello {name}")

df = pd.DataFrame({
    'first' : [1,2,3,4],
    'second' : [4,6,5,7]
     })
df.to_csv("sample.csv")
st.write(df)

file = st.file_uploader("choose a csv file",type='csv')
if file is not None:
    df = pd.read_csv(file)
    st.write(df)