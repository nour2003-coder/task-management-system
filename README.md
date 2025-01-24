# User and Task Management Application

## 🌟 Overview
The **User and Task Management System** is a web-based application designed to help users manage their tasks and profiles efficiently. Built using **Python** with **Streamlit** for a smooth web interface, and **Microsoft SQL Server** for reliable database management, this system allows users to register, log in, manage tasks, and update their profile information in a user-friendly environment.

---

## 🚀 Features
- **User Registration and Login**: Secure sign-up and login system to manage users.
- **Task Management**: Add, view, update, and delete tasks with ease.
- **Profile Management**: Update user information like name, address, phone number, and date of birth.

---

## 🏗️ System Architecture
The project consists of two main components:
1. **Database**: Manages user and task data efficiently.
2. **Web Application**: A user-friendly interface built using Streamlit for easy interaction.

### 📊 Database Design
The system's database consists of two primary tables:
- **`user_db`**: Stores user-related information such as username, password, name, address, phone number, and date of birth.
- **`task`**: Stores tasks associated with each user.

```sql
-- SQL Code for Table Creation

-- Create user_db Table
CREATE TABLE user_db (
    username NVARCHAR(50) PRIMARY KEY,
    Passworduser NVARCHAR(255) NOT NULL,
    Name NVARCHAR(255),
    address NVARCHAR(255),
    phone NVARCHAR(15),
    Datebirth DATE
);

-- Create task Table
CREATE TABLE task (
    task_id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50),
    description NVARCHAR(MAX),
    FOREIGN KEY (username) REFERENCES user_db(username) ON DELETE CASCADE
);
```

---

## 🔧 How It Works
The application is powered by Python, Streamlit, and SQL Server, providing a seamless user experience and efficient task management.

1. **User Registration**: Users can sign up by entering a unique username and password.
2. **Login**: Registered users can log in securely to access their profile and tasks.
3. **Task Management**: Users can create, update, and delete tasks associated with their profile.
4. **Profile Management**: Users can update their personal information, including name, address, and phone number.

---

## 🖥️ Application Flow
The core of the application is divided into two key files:
- **`connection.py`**: Manages database connections.
- **`rita.py`**: Contains the main logic for the user interface and task management.

### 🌐 Streamlit Application
Streamlit provides a clean and interactive interface for the following features:
- User registration and login.
- Profile management (view, update details, and change password).
- Task management (add, view, update, and delete tasks).

---

## 📦 Installation & Running the Project
To get the project up and running on your local machine:

1. **Install the required dependencies**:
    ```bash
    pip install streamlit pyodbc
    ```

2. **Set up the SQL Server database**:
    - Configure the database using the provided SQL schema.

3. **Run the Streamlit application**:
    ```bash
    streamlit run rita.py
    ```

4. **Access the application**:
    - Open the provided URL to use the app in your browser.

---

## 🎯 Conclusion
This project integrates Python and SQL Server to create an efficient task and user management system with a beautiful Streamlit interface. The modular design ensures flexibility for future feature extensions.

---

