import streamlit as st

st.title('Adjectives')

if 'counter' not in st.session_state:
    st.session_state.counter1 = 3


click1 = st.button('counter 1')
if click1:
    st.session_state.counter1 -=1

st.write(st.session_state.counter1)

