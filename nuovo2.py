from random import choice
import json,requests
import streamlit as st
from googletrans import Translator

st.title('Adjectives')

if 'counter1' not in st.session_state:
 st.session_state.counter1 = 3
if st.session_state.counter1 < 1:
 st.title('Game Over!')
 st.stop()

word_input = st.text_input('inserisci la tua traduzione: ','')


words = ['forte','alto','ricco']
if 'choice' not in st.session_state:
 st.session_state.choice = choice(words)
translator = Translator()
trans = translator.translate(st.session_state.choice,src='it', dest= 'en')
if 'word_trans' not in st.session_state:
 st.session_state.word_trans = trans.text
 
def new_word(new_word):
 st.session_state.choice = new_word
 new_trans = translator.translate(new_word,src='it', dest= 'en')
 st.session_state.word_trans = new_trans.text

word_pic = st.session_state.choice
pic_word = st.write(word_pic)

  
if word_input:
 if st.session_state.word_trans != word_input:
  st.session_state.counter1 -=1
  st.write('Sbagliato!')
 elif st.session_state.word_trans == word_input:
  new_word(choice(words))
  del pic_word
  word_pic = st.session_state.choice
  pic_word = st.write(word_pic)
  st.write('Esatto! Ora passiamo agli antonimi!')
  keyword=st.text_input('scrivi qui l\' antonimo: ','')
  url= 'https://api.datamuse.com/words?rel_ant=' + keyword + ''
  response = requests.get(url)
  datamuse = json.loads(response.text)
  if 'antonym' not in st.session_state:
   st.session_state.antonym = datamuse[0]['word']
  st.write(st.session_state.antonym)

st.write(st.session_state.counter1)
