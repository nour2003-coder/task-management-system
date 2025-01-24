import connection
import streamlit as st
from datetime import datetime
def register_user():
    st.subheader("---- Register ----")
    back=st.button("back")
    with st.form(key="register_form"):
        username = st.text_input('Enter your username',key='register_username')
        password = st.text_input('Enter your password', type='password', key='register_password')
        register_button = st.form_submit_button('register')
        

    if register_button:
        
        cursor.execute("SELECT * FROM user_db WHERE username = ?", (username,))
        if cursor.fetchone(): 
            st.error("Username already exists! Try again.")
            return
        if len(password) < 6:
            st.error("Password must be at least 6 characters long!")
            return
        try:
            sql_command = """INSERT INTO user_db (username, Passworduser) VALUES (?, ?);"""
            cursor.execute(sql_command, (username, password))
            conn.commit()  
            st.success("Registration successful!")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    if back:
        switch_page('home')
        st.experimental_rerun()

def login_user():
    st.subheader("---- Login ----")
    back=st.button("back")
    with st.form(key="login_form"):
        username = st.text_input('Enter your username', key='login_username')
        password = st.text_input('Enter your password', type='password', key='login_password')
        login_button = st.form_submit_button('Login')
        
    if login_button:
        cursor.execute("SELECT passworduser FROM user_db WHERE username = ?", (username,))
        user = cursor.fetchone()
        if not user:
            st.error("Username not found! Please register first.")
            return
        if user[0] == password:
            st.session_state.page = 'dashboard'
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error("Incorrect password! Try again.")
    if back:
        switch_page('home')
        st.experimental_rerun()

# Dashboard after successful login
def user_dashboard(username):
    st.subheader(f"--- Dashboard: {username} ---")
    if st.button("View Profile"):
        st.session_state.page = 'view_profile'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("change password"):
        st.session_state.page = 'change_password'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("Manage tasks"):
        st.session_state.page = 'manage_tasks'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("Update Profile Details"):
        st.session_state.page = 'update_Profile_Details'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("back"):
        switch_page('home')
        st.experimental_rerun()

 


def view_profile(username):
    st.subheader(f"\n--- Profile ---")
    
    # Execute the SQL query to fetch the user's data
    cursor.execute("SELECT username, name, address, phone, Datebirth FROM user_db WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        st.write(f"Username: {user[0]}")
        st.write(f"Name: {user[1] or ''}")  
        st.write(f"Address: {user[2] or ''}") 
        st.write(f"Phone: {user[3] or ''}")  
        st.write(f"Date of Birth: {user[4] or ''}")  
    else:
        st.error("Profile not found!")
    back=st.button("Back")
    if back:
        switch_page('dashboard')
        st.experimental_rerun()

# View Tasks
def view_tasks(username):
    st.subheader("--- Your Tasks ---")
    back=st.button("Back")
    if back:
        switch_page('manage_tasks')
        st.experimental_rerun()

    cursor.execute("SELECT description FROM task WHERE username = ?", username)
    tasks = cursor.fetchall()

    if not tasks:
        st.write("No tasks available.")
    else:
        for i, task in enumerate(tasks, start=1):
            st.write(f"{i}. {task[0]}")  

# Update Profile Details
def update_profile_details(username):
    st.subheader("\n--- Update Profile Details ---")
    back=st.button("back")
    # Fetch current profile data
    cursor.execute("SELECT Name, address, phone, Datebirth FROM user_db WHERE username = ?", (username,))
    user_data = cursor.fetchone()

    if not user_data:
        st.error("No profile details found!")
        return
    if isinstance(user_data[3], str):
        dob = datetime.strptime(user_data[3], "%Y-%m-%d").date()
    else:
        dob = user_data[3]  # Assuming it's already a date object
    with st.form(key="edit_form"):
        name = st.text_input("New Name: ",placeholder=user_data[0] or "") or user_data[0]
        address = st.text_input("New Address: ",placeholder=user_data[1] or "") or user_data[1]
        phone = st.text_input("New Phone number: ",placeholder=user_data[2] or "") or user_data[2]
        dob = st.date_input("New Date of Birth: ",value=dob if dob else None) or dob
        edit_button = st.form_submit_button('edit')
    if edit_button:
        if dob > datetime.now().date():
            st.error("Invalid Date of Birth! Please select a valid date of birth that is not in the future.")
            return
        if "+" not in phone :
            st.error("Invalid Phone Number! The phone number must contain a '+' symbol, e.g., '+123456789'.")
            return
        try:
            # Update the profile in the database
            sql_command = """
            UPDATE user_db 
            SET Name = ?, address = ?, phone = ?, Datebirth = ? 
            WHERE username = ?;
            """
            cursor.execute(sql_command, (name, address, phone, dob, username))
            conn.commit()  # Commit changes to the database

            st.success("Profile updated successfully!")
        except Exception as e:
                st.error(f"An error occurred: {e}")
    if back:
        switch_page('dashboard')
        st.experimental_rerun()

# Change Password
def change_password(username):
    st.subheader("\n--- Change Password ---")
    back=st.button("Back")
    if back:
        switch_page('dashboard')
        st.experimental_rerun()
    with st.form(key="change_pass"):
        old_password = st.text_input("Enter your current password: ",type="password",key='old_password')
        new_password = st.text_input("Enter the new password: ",type="password",key='new_password')
        pass_button=st.form_submit_button("change password")
    if pass_button:
        cursor.execute("SELECT Passworduser FROM user_db WHERE username = ?", (username,))
        db_password = cursor.fetchone()

        if db_password and (db_password[0] == old_password):   
            if len(new_password) < 6:
                st.error("Password must be at least 6 characters long!")
                return

            sql_command = """UPDATE user_db SET Passworduser = ? WHERE username = ?;"""
            cursor.execute(sql_command, (new_password, username))
            conn.commit()  

            st.success("Password updated successfully!")
        else:
            st.error("Incorrect current password! Password not changed.")

# Manage Tasks
def manage_tasks(username):
    st.subheader("--- Task Management ---")
    if st.button("View Tasks"):
        st.session_state.page = 'view_Tasks'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("Add Task"):
        st.session_state.page = 'add_task'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("Update Task"):
        st.session_state.page = 'update_task'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("Delete Task"):
        st.session_state.page = 'delete_task'
        st.session_state.username = username
        st.experimental_rerun()
    if st.button("Back to Dashboard"):
        switch_page('dashboard')
        st.experimental_rerun()

# Add Task
def add_task(username):
    st.subheader("--- Add Task ---")
    back=st.button("Back")
    if back:
        switch_page('manage_tasks')
        st.experimental_rerun()
    with st.form(key="add_form"):
        task = st.text_input("Enter a new task: ")
        submit_button=st.form_submit_button("submit")
    
    try:
        if submit_button:   
            cursor.execute("SELECT * FROM task WHERE description = ? and username= ?", (task,username,))
            if cursor.fetchone(): 
                st.warning("task already exists!")
                return
            sql_command = """INSERT INTO task (username, description) VALUES (?, ?);"""
            cursor.execute(sql_command, (username, task))
            conn.commit()  
            st.success(f"Task '{task}' added successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")
# Update Task
def update_task(username):
    st.subheader("--- Update Task ---")
    back=st.button("Back")
    if back:
        switch_page('manage_tasks')
        st.experimental_rerun()
    cursor.execute("SELECT description FROM task WHERE username = ?", username)
    tasks = cursor.fetchall()

    if not tasks:
        st.write("No tasks available.")
    else:
        task_descriptions = [task[0] for task in tasks]  
        selected_task = st.radio("Select a task to update:", task_descriptions)

        # Input box for new task description
        new_task = st.text_input("Enter new task description:", value=selected_task)
        if st.button("Update Task"):
            if new_task.strip() == "":
                st.error("Task description cannot be empty!")
            elif new_task == selected_task:
                st.warning("No changes made. Please provide a different task description.")
            else:
                try:
                    sql_command = """UPDATE task SET description = ? WHERE username = ? AND description = ?;"""
                    cursor.execute(sql_command, (new_task, username, selected_task))
                    conn.commit() 

                    st.success(f"Task '{selected_task}' updated to '{new_task}' successfully!")
                    st.experimental_rerun()  # Refresh the page to reflect changes
                except Exception as e:
                    st.error(f"An error occurred: {e}")


# Delete Task
def delete_task(username):
    st.subheader("--- Delete Task ---")
    back=st.button("Back")
    if back:
        switch_page('manage_tasks')
        st.experimental_rerun()
    cursor.execute("SELECT description FROM task WHERE username = ?", username)
    tasks = cursor.fetchall()

    if not tasks:
        st.write("No tasks available.")
    else:
        task_descriptions = [task[0] for task in tasks]  
        selected_task = st.radio("Select a task to delete:", task_descriptions)
        if st.button("Delete Task"):
                try:
                    sql_command = """DELETE FROM task WHERE username = ? and description = ?;"""
                    cursor.execute(sql_command, (username, selected_task))
                    conn.commit() 

                    st.success("Task  deleted successfully!")
                    st.experimental_rerun()  
                except Exception as e:
                    st.error(f"An error occurred: {e}")

# Function to switch pages
def switch_page(page_name):
    st.session_state.page = page_name
conn = connection.connect_to_db()
cursor = conn.cursor()


# Initialize session state for page tracking if it doesn't exist
if 'page' not in st.session_state:
    st.session_state.page = 'home' 
if st.session_state.page == 'home':
    st.title("Welcome")
    st.button("Register", on_click=lambda: switch_page("register"))
    st.button("Login", on_click=lambda: switch_page("login"))

elif st.session_state.page == 'register':
    register_user()

elif st.session_state.page == 'login':
    login_user()
elif st.session_state.page == 'dashboard' and st.session_state.username:
    user_dashboard(st.session_state.username)
elif st.session_state.page == 'view_profile' and st.session_state.username:
    view_profile(st.session_state.username)
elif st.session_state.page == 'change_password' and st.session_state.username:
    change_password(st.session_state.username)
elif st.session_state.page == 'manage_tasks' and st.session_state.username:
    manage_tasks(st.session_state.username)
elif st.session_state.page == 'update_Profile_Details' and st.session_state.username:
    update_profile_details(st.session_state.username)
elif st.session_state.page == 'view_Tasks' and st.session_state.username:
    view_tasks(st.session_state.username)
elif st.session_state.page == 'add_task' and st.session_state.username:
    add_task(st.session_state.username)
elif st.session_state.page == 'update_task' and st.session_state.username:
    update_task(st.session_state.username)
elif st.session_state.page == 'delete_task' and st.session_state.username:
    delete_task(st.session_state.username)

cursor.close()  
conn.close()  
