import streamlit as st
st.markdown("""   
<style>
            .stButton> button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }

</style>


""", unsafe_allow_html=True)

# st.title("Hello, Streamlit!")
st.title("Form")


name= st.text_input("Enter your name: ", key="Name")
email= st.text_input("Enter your email: ", key="Email")
age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Nashik", "Pune", "Mumbai","Delhi"])
if st.button("Submit"):
    st.write("Your name is ",name)
    st.write("Your email is ",email)
    st.write("Your age is ",age)
    st.write("Your city is ",city)