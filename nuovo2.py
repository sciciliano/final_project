from random import choice
import streamlit as st
from googletrans import Translator

word_input = st.text_input('inserisci la tua traduzione: ','')


words = ['mela','pera','pomodoro']
if 'choice' not in st.session_state:
 st.session_state.choice = choice(words)
 word_pic = st.session_state.choice
 translator = Translator()
 trans = translator.translate(word_pic,src='it', dest= 'en')
 if 'word_trans' not in st.session_state:
  st.session_state.word_trans = trans.text
 
def new_word(new_word):
 st.session_state.choice = new_word
 word_pic = st.session_state.choice
 trans = translator.translate(word_pic,src='it', dest= 'en')
 st.session_state.word_trans = trans.text

pic_word = st.write(word_pic)
  
if word_input:
 if st.session_state.word_trans == word_input:
  st.write('Esatto!')
  new_word(choice(words))
    
 elif st.session_state.word_trans != word_input:
  st.write('Sbagliato!')
