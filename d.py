import streamlit as st

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Function to switch pages
def switch_page(page_name):
    st.session_state.page = page_name

# Registration Page
def register_user():
    st.subheader("---- Register ----")
    with st.form(key="register_form"):
        username = st.text_input('Enter your username', key='register_username')
        password = st.text_input('Enter your password', type='password', key='register_password')
        register_button = st.form_submit_button('Register')

    if register_button:
        # Simulate database check and user creation
        st.success(f"User {username} registered successfully!")
        switch_page("login")  # Navigate to login page after registration

# Login Page
def login_user():
    st.subheader("---- Login ----")
    with st.form(key="login_form"):
        username = st.text_input('Enter your username', key='login_username')
        password = st.text_input('Enter your password', type='password', key='login_password')
        login_button = st.form_submit_button('Login')

    if login_button:
        # Simulate login check
        if username == "admin" and password == "password":  # Example credentials
            st.success(f"Welcome, {username}!")
            switch_page("dashboard")  # Navigate to dashboard on successful login
        else:
            st.error("Invalid username or password.")

# Dashboard Page
def user_dashboard():
    st.subheader("--- Dashboard ---")
    st.write("Welcome to the dashboard!")
    if st.button("Logout"):
        switch_page("home")  # Navigate back to home on logout

# Navigation Logic



