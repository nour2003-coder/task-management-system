import streamlit as st

# Create a slider
x = st.slider('Select a value', 0, 100, 50)
st.write(f'The selected value is: {x}')

# Text input field
name = st.text_input('Enter your name')
st.write(f'Hello, {name}!')
st.title('My First Streamlit App')

# Add a subtitle
st.subheader('Streamlit makes it easy to create interactive web apps.')

# Add some text
st.write("This is a simple example to show Streamlit basics.")
