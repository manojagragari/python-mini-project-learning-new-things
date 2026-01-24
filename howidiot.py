import random
import streamlit as st
st.title("how idior are you")
st.chat_inputx=st.text_input("Enter a name")
if(st.button("Get result")):
    st.success(F"IDIOT SCORE : {random.randint(0,100)} %")