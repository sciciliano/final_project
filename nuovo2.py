from random import choice
import streamlit as st
from googletrans import Translator

words = ['mela','pera','pomodoro']
word_pic = choice(words)
st.write(word_pic)

translator = Translator()
word_trans = translator.translate(word_pic,src='it', dest= 'en')

word_input = st.text_input('inserisci la tua traduzione: ','')

if (word_trans and word_input):
  if word_trans.text == word_input:
    st.write('Esatto!')
  elif word_trans.text != word_input:
    st.write('Sbagliato!')
