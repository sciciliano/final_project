from random import choice
import streamlit as st
from googletrans import Translator

word_input = st.text_input('inserisci la tua traduzione: ','')

translator = Translator()
words = ['mela','pera','pomodoro']
word_pic = choice(words)
trans = translator.translate(word_pic,src='it', dest= 'en')
if 'word_trans' not in st.session_state:
 st.session_state.word_trans = trans.text


if word_input:
  if st.session_state.word_trans == word_input:
    st.write('Esatto!')
    st.session_state.word_pic = choice(words)
  elif st.session_state.word_trans != word_input:
    st.write('Sbagliato!')
