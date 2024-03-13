import streamlit as st
import openai
import os
from openai import OpenAI
from dotenv import load_dotenv
import time
import base64
load_dotenv()   
#st.caption('This is your one-stop solution for film production processes, enhanced with AI integration.')

def MyBG_colour(wch_colour): 
    my_colour = f"<style> .stApp {{background-color: {wch_colour};}} </style>"
    st.markdown(my_colour, unsafe_allow_html=True)

MyBG_colour("#9eedf7")

st.title('Generativerse.ai')
st.text('Welcome to Maths Tutor Assistant by OpenAI') 
prompt = st.chat_input("Say something")
client=OpenAI()
assistant = client.beta.assistants.retrieve("asst_n9gI5cHsnLOtEF2Gajz4autP")
if prompt:
    st.write(f"Input: {prompt}")
    #openai.api_key = os.getenv('OPENAI_API_KEY')
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(thread_id=thread.id,role="user",
    content=prompt)
    
    try:
        run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,
                                          instructions="Please address the user as Jane Doe. The user has a premium account.")
        while run.status != "completed":
            print(run.status)
            time.sleep(5)
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        #run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        assistant_messages_for_run = [
            message for message in messages 
            if message.run_id == run.id and message.role == "assistant"
        ]
        for message in assistant_messages_for_run:
            message_content = message.content[0].text.value
            st.markdown(message_content, unsafe_allow_html=True)

    except Exception as e:
        st.text(e)
        st.text({"error": "Failed to process your request"}) 
st.image(r"C:\Users\dilee\Documents\OpenAI-Assistant-Integration\Assistant-Integration.png")