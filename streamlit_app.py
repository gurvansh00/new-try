import streamlit as st
mysp=__import__("my-voice-analysis")
import openai

messages = [ {"role": "system", "content":  
              "You are a intelligent assistant."} ] 
'''while True: 
    message = input("User : ") 
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})'''
st.title("My Voice")
st.text_input("Enter the topic of the speech", value="")
col = st.columns(2)
st.write("What is the intent of you speech")
intent = st.selectbox('',('Inform', 'Persuade', 'Entertain','Educate'))
st.write("What is the mood of your
