import streamlit as st


count = 3
if count not in st.session_state:
  st.session_state[count] = -1
st.write(st.session_state.count)
