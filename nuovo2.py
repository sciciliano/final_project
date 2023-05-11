from random import choice
import streamlit as st
from googletrans import Translator

word_input = st.text_input('inserisci la tua traduzione: ','')

translator = Translator()
words = ['mela','pera','pomodoro']
word_pic = choice(words)
st.write(word_pic)
word_trans = translator.translate(word_pic,src='it', dest= 'en')

if word_input:
  if word_trans.text == word_input:
    st.write('Esatto!')
  elif word_trans.text != word_input:
    st.write('Sbagliato!')