import streamlit as st

# Title
st.title("Streamlit Form Example")

# Creating a form
with st.form("my_form"):
    st.header("User Input Form")
    
    # Input fields
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0, max_value=100, step=1)
    gender = st.selectbox("Select your gender:", ["Male", "Female", "Other"])
    feedback = st.text_area("Any additional feedback?")

    # Submit button
    submitted = st.form_submit_button("Submit")

# Handling form submission
if submitted:
    st.success("Form submitted successfully!")
    st.write("### Submitted Data:")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Feedback:** {feedback}")

