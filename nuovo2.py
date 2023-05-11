from random import choice
import streamlit as st
from googletrans import Translator

word_input = st.text_input('inserisci la tua traduzione: ','')

translator = Translator()
words = ['mela','pera','pomodoro']
if 'word_pic' not in st.session_state:
 st.session_state.word_pic = choice(words)
st.write(st.session_state.word_pic)
word_trans = translator.translate(st.session_state.word_pic,src='it', dest= 'en')

if word_input:
  if word_trans.text == word_input:
    st.write('Esatto!')
    st.session_state.word_pic = choice(words)
  elif word_trans.text != word_input:
    st.write('Sbagliato!')
