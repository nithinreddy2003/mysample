import streamlit as st
st.header('RAMACHANDRA COLLEGE OF ENGINEERING')
a=st.number_input("Enter Any Value")
if st.button("HIT ME"):
  st.success(f'Your Lucky Number Is {a}')
