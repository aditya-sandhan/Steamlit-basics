import streamlit as st

st.title("Simple chatbot")
Question= st.text_input("Ask me anything: ", key="question")    

if st.button("Start Chatting"):
    st.write(f"You asked: {Question}")
    st.write("chatbot is thinking...")