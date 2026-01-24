import random
import streamlit as st
st.title("Random Number Generator(frendship percentage)")
x=st.text_input("Your first name")
y=st.text_input("Your last name")
if st.button("Calculate Friendship Percentage"):
    st.success(f"your frendship score is,{random.randint(0,100)}%")