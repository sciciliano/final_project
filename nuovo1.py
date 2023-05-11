import streamlit as st

st.title('Adjectives')

if 'counter' not in st.session_state:
    st.session_state.counter1 = 3
    st.session_state.counter2 = 3
if st.session_state.counter1 < 1 or st.session_state.counter2 < 1:
    st.title('Game Over!')
    st.stop()

click1 = st.button('counter 1')
click2 = st.button('counter 2')

if click1:
    st.session_state.counter1 -=1

if click2:
    st.session_state.counter2 -=1

st.write(st.session_state.counter1)
st.write(st.session_state.counter2)
