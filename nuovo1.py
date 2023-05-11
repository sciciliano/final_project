import streamlit as st

st.title('Adjectives')

if 'counter1' not in st.session_state or 'counter2' not in st.session_state :
    st.session_state.counter1 = 3
    st.session_state.counter2 = 3
if st.session_state.counter1 < 2 or st.session_state.counter2 < 2:
    st.title('Game Over!')
    st.stop()

click1 = st.button('counter 1')
if click1:
    st.session_state.counter1 -=1
click2 = st.button('counter 2')
if click2:
    st.session_state.counter2 -=1

st.write(st.session_state.counter1)
st.write(st.session_state.counter2)
