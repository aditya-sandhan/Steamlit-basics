import streamlit as st

st.title("Basic calculator")

num1 = st.number_input("Enter first number: ", step=1, format="%d")
num2 = st.number_input("Enter second number: ", step=1, format="%d")

Operations = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

if st.button("Calculate"):
    if Operations == "Addition":
        st.write(f"The result of {num1} + {num2} is: {num1 + num2}")
    elif Operations == "Subtraction":
        st.write(f"The result of {num1} - {num2} is: {num1 - num2}")
    elif Operations == "Multiplication":
        st.write(f"The result of {num1} * {num2} is: {num1 * num2}")
    elif Operations == "Division":
        if num2 != 0 :
            st.write(f"The result of {num1} / {num2} is: {num1 / num2}")
        else:
            st.write("Error: Division by zero is not allowed.")