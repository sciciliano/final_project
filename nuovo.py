import streamlit as st
import json, requests
from googletrans import Translator
from random import choice

st.title('Adjectives')

if 'counter' not in st.session_state:
    st.session_state.counter = 3
if st.session_state.counter < 1:
    st.title('Game Over!')
    st.stop()

translator = Translator()
keywords = ['bella','lungo','agile']
var = choice(keywords)

adj_trans = translator.translate(var,dest='en')
adj_answer = st.text_input('Write your answer here:','')

if adj_answer is not None:
    if adj_answer == adj_trans:
        feedback = st.write('Right!')
    elif adj_answer  != adj_trans:
        feedback = st.write('Nope, try again!')
        st.session_state.counter -= 1

st.write(st.session_state.counter)
