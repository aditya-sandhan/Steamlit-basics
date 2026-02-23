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
st.title("Welcome to your first Streamlit app.")

age = st.slider("Select your age", 1, 100)
city = st.selectbox("Select your city", ["Nashik", "Pune", "Mumbai","Delhi"])

if st.button("Submit"):
    st.write("Your age is ",age)
    st.write("Your city is ",city)