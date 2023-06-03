import tkinter as tk
import pyttsx3
import speech_recognition as sr

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio= rec.listen(source,phrase_time_limit=5)
            text = rec.recognize_google(audio, language='en-US')
            text = text.lower()
        except sr.UnknownValueError:
            text = 'something went wrong, sorry'
        except sr.RequestError:
            text = 'something went wrong, sorry'
    engine = pyttsx3.init()
    voice = engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)
    if 'close' in text:
        engine.say('Command executed: Door closed')
    elif 'open' in text:
        engine.say('Command executed: Door open')
    else:
        engine.say('sorry, I didn\'t understand')
    engine.runAndWait()

gui = tk.Tk()
gui.title("UniBz Chatbot")
gui.iconbitmap('unibz.ico')
gui.geometry("800x400")
gui.resizable(0,0)
gui.configure(bg='#2c4557')
listen_Button=tk.Button(gui,text='mic',borderwidth=0,activebackground='#2c4557',command=listen)
listen_Button.place(x=380,y=300)

gui.mainloop()
