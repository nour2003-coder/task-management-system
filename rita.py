import connection
import streamlit as st
# Register User
import streamlit as st
import sqlite3  # or the database you're using

def register_user():
    st.subheader("---- Register ----")
    
    # Get user inputs
    username = st.text_input('Enter your username')
    password = st.text_input('Enter your password', type='password')

    # Check if a button is clicked
    if st.button('Register', key='register_button'):
        
        # Check if the username is already in the database
        cursor.execute("SELECT * FROM user_db WHERE username = ?", (username,))
        if cursor.fetchone():  # If the username already exists
            st.write("Username already exists! Try again.")
            return
        
        # Validate password length
        if len(password) < 6:
            st.write("Password must be at least 6 characters long!")
            return
        
        # Insert the new user into the database
        try:
            sql_command = """INSERT INTO user_db (username, Passworduser) VALUES (?, ?);"""
            cursor.execute(sql_command, (username, password))
            conn.commit()  # Commit the transaction to the database
            st.write("Registration successful!")
        except Exception as e:
            st.write(f"An error occurred: {e}")



# Login User and validate credentials from SQL Server
def login_user():
    st.subheader("---- Login ----")

    username = st.text_input('Enter your username')
    password = st.text_input('Enter your password', type='password')

    if st.button('login', key='login_button'):
        cursor.execute("SELECT passworduser FROM user_db WHERE username = ?", username)
        user = cursor.fetchone()
        if not user:
            st.write("Username not found! Please register first.")
            return
     
        if user[0] == password:
            st.write(f"\nWelcome back, {username}!")
            st.session_state.page = 'user_dashboard'
            user_dashboard(username)
        else:
            st.write("Incorrect password! Try again.")

# Dashboard after successful login
def user_dashboard(username):
    st.subheader(f"\n--- Dashboard: {username} ---")
    if st.button("View Profile"):
        st.session_state.page = 'view'
        view_profile(username)
    elif st.button("change password"):
        st.session_state.page = 'change_password'
        change_password(username)
    elif st.button("Manage tasks"):
        st.session_state.page = 'manage_tasks'
        manage_tasks(username)
    elif st.button("Update Profile Details"):
        st.session_state.page = 'Update_Profile_Details'
        update_profile_details(username)
    elif st.button("back"):
        st.write(f"Goodbye, {username}!")


# View Profile
def view_profile(username):
    print(f"\n--- Profile ---")
    cursor.execute("SELECT username, name, address, phone, Datebirth FROM user_db WHERE username = ?", username)
    user = cursor.fetchone()

    if user:
        print(f"Username: {user[0]}")
        print("Name: ",{user[1] or ""})
        print(f"Address: {user[2] or ""}")
        print(f"Phone: {user[3] or ""}")
        print(f"Date of Birth: {user[4] or ""}")
    else:
        print("Profile not found!")

# View Tasks
def view_tasks(username):
    print("\n--- Your Tasks ---")
    cursor.execute("SELECT description FROM task WHERE username = ?", username)
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task[0]}")  # task[0] contains the task description

# Update Profile Details
def update_profile_details(username):
    print("\n--- Update Profile Details ---")

    # Fetch current profile data
    cursor.execute("SELECT Name, address, phone, Datebirth FROM user_db WHERE username = ?", (username,))
    user_data = cursor.fetchone()

    if not user_data:
        print("No profile details found!")
        return

    # Ask for new profile details
    name = input(f"Current Name: {user_data[0]}\nNew Name: ") or user_data[0]
    address = input(f"Current Address: {user_data[1]}\nNew Address: ") or user_data[1]
    phone = input(f"Current Phone: {user_data[2]}\nNew Phone: ") or user_data[2]
    dob = input(f"Current Date of Birth: {user_data[3]}\nNew Date of Birth: ") or user_data[3]

    # Update the profile in the database
    sql_command = """
    UPDATE user_db 
    SET Name = ?, address = ?, phone = ?, Datebirth = ? 
    WHERE username = ?;
    """
    cursor.execute(sql_command, (name, address, phone, dob, username))
    conn.commit()  # Commit changes to the database

    print("Profile updated successfully!")

# Change Password
def change_password(username):
    print("\n--- Change Password ---")
    old_password = input("Enter your current password: ")

    # Verify current password
    cursor.execute("SELECT Passworduser FROM user_db WHERE username = ?", (username,))
    db_password = cursor.fetchone()

    if db_password and (db_password[0] == old_password):
        new_password = input("Enter a new password: ")
        if len(new_password) < 6:
            print("Password must be at least 6 characters long!")
            return

        # Update the password in the database
        sql_command = """UPDATE user_db SET Passworduser = ? WHERE username = ?;"""
        cursor.execute(sql_command, (new_password, username))
        conn.commit()  # Commit changes to the database

        print("Password updated successfully!")
    else:
        print("Incorrect current password! Password not changed.")

# Manage Tasks
def manage_tasks(username):
    while True:
        print("\n--- Task Management ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Back to Dashboard")
        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")
        if choice == "1":
            view_tasks(username)
        elif choice == "2":
            add_task(username)
        elif choice == "3":
            update_task(username)
        elif choice == "4":
            delete_task(username)
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

# Add Task
def add_task(username):
    print("\n--- Add Task ---")
    task = input("Enter a new task: ")

    # Insert task into the database
    sql_command = """INSERT INTO task (username, description) VALUES (?, ?);"""
    cursor.execute(sql_command, (username, task))
    conn.commit()  # Commit changes to the database

    print(f"Task '{task}' added successfully!")

# Update Task
def update_task(username):
    print("\n--- Update Task ---")
    task_id = input("Enter the task  to update: ")
    new_task = input("Enter the new task description: ")

    # Update the task in the database
    sql_command = """UPDATE task SET description = ? WHERE username = ? AND description = ?;"""
    cursor.execute(sql_command, (new_task, username, task_id))
    conn.commit()  # Commit changes to the database

    print(f"Task {task_id} updated successfully!")

# Delete Task
def delete_task(username):
    print("\n--- Delete Task ---")
    task_id = input("Enter the task  to delete: ")

    # Delete the task from the database
    sql_command = """DELETE FROM task WHERE username = ? and description = ?;"""
    cursor.execute(sql_command, (username, task_id))
    conn.commit()  # Commit changes to the database

    print(f"Task {task_id} deleted successfully!")

# Main flow
conn = connection.connect_to_db()
cursor = conn.cursor()
import streamlit as st

# Initialize session state for page tracking if it doesn't exist
if 'page' not in st.session_state:
    st.session_state.page = 'home' 


# Page navigation logic
if st.button('Register'):
    st.session_state.page = 'register'
    register_user()
if st.button('Login'):
    st.session_state.page = 'login'
    login_user()

cursor.close()  
conn.close()  
